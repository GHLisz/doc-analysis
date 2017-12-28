import unittest
from entry import Entry
from wrange import WRange
from char_set_util import CharSetUtil


class Doc:
    def __init__(self):
        self.app, self.doc = self.get_app_and_doc()
        self.manual_content_range = self.get_manual_content_range()
        self.toc_range = self.get_toc_range()
        self.manual_content_entries = self.get_bookmarks_in_range(self.manual_content_range)
        self.toc_entries = self.get_bookmarks_in_range(self.toc_range)
        self.stuff_mc_entries()
        self.stuff_toc_entries()

    def get_bookmarks_in_range(self, wrange):
        app, doc = self.app, self.doc
        app.Selection.SetRange(wrange.start, wrange.end)

        bookmarks = []
        for link in app.Selection.Hyperlinks:
            bookmarks.append(link.name)

        return [Entry(b) for b in bookmarks]

    def get_manual_content_range(self):
        app, doc = self.app, self.doc

        old_doc_end = doc.Content.End
        manual_content_start = doc.TablesOfContents(1).Range.End + 1

        app.Selection.SetRange(manual_content_start, manual_content_start)
        self.insert_manual_content()

        new_doc_end = doc.Content.End
        manual_content_length = new_doc_end - old_doc_end
        manual_content_end = manual_content_start + manual_content_length

        return WRange(manual_content_start, manual_content_end)

    def get_toc_range(self):
        return WRange(self.doc.TablesOfContents(1).Range.Start,
                      self.doc.TablesOfContents(1).Range.End)

    def stuff_entries(self):
        app, doc = self.app, self.doc
        contains_cn = CharSetUtil().contains_cn

        para_idx = 0
        for para in doc.Paragraphs:
            para_idx += 1

            para_outline_level = para.OutlineLevel
            if para_outline_level == 10:
                continue

            bookmarks = [b.name for b in para.Range.Bookmarks]
            used_bookmarks = [b for b in bookmarks if (
                              (b in [e.bookmark_name for e in self.manual_content_entries])
                              or (b in [e.bookmark_name for e in self.toc_entries]))]

            if not used_bookmarks:
                continue

            if not contains_cn(para.Range.Text):
                continue

            for bookmark in used_bookmarks:
                for entry in self.manual_content_entries:
                    if bookmark == entry.bookmark_name:
                        entry.append_paragraph_outline_level((para_idx, para_outline_level))
                for entry in self.toc_entries:
                    if bookmark == entry.bookmark_name:
                        entry.append_paragraph_outline_level((para_idx, para_outline_level))

    def stuff_mc_entries(self):
        app, doc = self.app, self.doc

        para_idx = 0
        for para in doc.Paragraphs:
            para_idx += 1
            para_outline_level = para.OutlineLevel

            bookmarks = [b.name for b in para.Range.Bookmarks]
            used_bookmarks = [b for b in bookmarks if (
                              (b in [e.bookmark_name for e in self.manual_content_entries])
                              )]

            if not used_bookmarks:
                continue

            for bookmark in used_bookmarks:
                for entry in self.manual_content_entries:
                    if bookmark == entry.bookmark_name:
                        entry.append_paragraph_outline_level((para_idx, para_outline_level))

    def stuff_toc_entries(self):
        app, doc = self.app, self.doc
        contains_cn = CharSetUtil().contains_cn

        para_idx = 0
        for para in doc.Paragraphs:
            para_idx += 1

            para_outline_level = para.OutlineLevel
            if para_outline_level == 10:
                continue

            bookmarks = [b.name for b in para.Range.Bookmarks]
            used_bookmarks = [b for b in bookmarks if (
                              (b in [e.bookmark_name for e in self.toc_entries])
                            )]

            if not used_bookmarks:
                continue

            if not contains_cn(para.Range.Text):
                continue

            for bookmark in used_bookmarks:
                for entry in self.toc_entries:
                    if bookmark == entry.bookmark_name:
                        entry.append_paragraph_outline_level((para_idx, para_outline_level))

    @staticmethod
    def get_app_and_doc():
        from win32com.client import Dispatch
        app = Dispatch('kwps.Application')
        app.Visible = 1
        app.DisplayAlerts = 0
        assert app.Documents.Count == 1, "Doc count check failed"
        doc = app.ActiveDocument
        doc.Bookmarks.ShowHidden = True
        assert doc.TablesOfContents.Count > 0, "Toc count check failed."
        return app, doc

    @staticmethod
    def insert_manual_content():
        import xmlrpclib
        try:
            wps_app = xmlrpclib.ServerProxy("http://127.0.0.1:60000")
            r = wps_app.InsertManualContent(3)
            return True
        except:
            raise EnvironmentError("insert_manual_content: RPC call failed.")


class DocTestCase(unittest.TestCase):
    def test_init(self):
        # kill all wps processes first
        self.assertRaises(EnvironmentError, Doc)


if __name__ == '__main__':
    unittest.main()

