#coding=utf-8
import unittest

from collections import defaultdict


class Doc:
    def __init__(self, range_list_of_level):
        self.range_list_of_level = range_list_of_level
        self.raw_sentence_data = defaultdict(list)
        self.raw_para_data = defaultdict(list)
        self.parse_ranges_of_key()

    @staticmethod
    def get_app_and_doc():
        from win32com.client import Dispatch
        app = Dispatch('kwps.Application')
        app.Visible = 1
        app.DisplayAlerts = 0
        doc = app.ActiveDocument
        return app, doc

    def parse_ranges_of_key(self):
        app, doc = self.get_app_and_doc()

        for k, v in self.range_list_of_level.items():
            for range_ in v:
                app.Selection.SetRange(range_[0], range_[1])

                paragraph = app.Selection.Paragraphs(1)
                paragraph_properties = [paragraph.TabStops.Count,
                                        paragraph.TabStops(1).Position,
                                        paragraph.TabStops(1).Alignment,
                                        paragraph.TabStops(1).Leader,
                                        paragraph.Alignment,
                                        paragraph.OutlineLevel,
                                        paragraph.ReadingOrder,
                                        paragraph.CharacterUnitLeftIndent,
                                        paragraph.CharacterUnitRightIndent,
                                        paragraph.LeftIndent,
                                        paragraph.CharacterUnitFirstLineIndent,
                                        paragraph.FirstLineIndent,
                                        paragraph.LineUnitBefore,
                                        paragraph.SpaceBefore,
                                        paragraph.LineUnitAfter,
                                        paragraph.SpaceAfter,
                                        paragraph.LineSpacingRule,
                                        paragraph.LineSpacing,
                                        paragraph.WidowControl,
                                        paragraph.KeepWithNext,
                                        paragraph.KeepTogether,
                                        paragraph.PageBreakBefore,
                                        paragraph.FarEastLineBreakControl,
                                        paragraph.WordWrap,
                                        paragraph.HangingPunctuation,
                                        paragraph.HalfWidthPunctuationOnTopOfLine,
                                        paragraph.AddSpaceBetweenFarEastAndAlpha,
                                        paragraph.BaseLineAlignment, ]
                self.raw_para_data[k].append(paragraph_properties)

                for sentence in app.Selection.Sentences:
                    sentence_properties = [sentence.Font.Name,
                                           sentence.Font.NameAscii,
                                           sentence.Font.NameBi,
                                           sentence.Font.BoldBi,
                                           sentence.Font.ItalicBi,
                                           sentence.Font.SizeBi,
                                           sentence.Font.Bold,
                                           sentence.Font.Italic,
                                           sentence.Font.Size,
                                           sentence.Font.Underline,
                                           sentence.Font.EmphasisMark,
                                           sentence.Font.StrikeThrough,
                                           sentence.Font.DoubleStrikeThrough,
                                           sentence.Font.Superscript,
                                           sentence.Font.Subscript,
                                           sentence.Font.SmallCaps,
                                           sentence.Font.AllCaps,
                                           sentence.Font.Hidden,
                                           sentence.Font.Scaling,
                                           sentence.Font.Spacing,
                                           sentence.Font.Position, ]
                    self.raw_sentence_data[k].append(sentence_properties)



    def parse_ranges(self, range_list):
        app, doc = self.get_app_and_doc()

        sentence_property_set = set()
        paragraph_property_set = set()

        for range_ in range_list:
            app.Selection.SetRange(range_[0], range_[1])

            paragraph = app.Selection.Paragraphs(1)
            paragraph_properties = [paragraph.TabStops.Count,
                                    paragraph.TabStops(1).Position,
                                    paragraph.TabStops(1).Alignment,
                                    paragraph.TabStops(1).Leader,
                                    paragraph.Alignment,
                                    paragraph.OutlineLevel,
                                    paragraph.ReadingOrder,
                                    paragraph.CharacterUnitLeftIndent,
                                    paragraph.CharacterUnitRightIndent,
                                    paragraph.LeftIndent,
                                    paragraph.CharacterUnitFirstLineIndent,
                                    paragraph.FirstLineIndent,
                                    paragraph.LineUnitBefore,
                                    paragraph.SpaceBefore,
                                    paragraph.LineUnitAfter,
                                    paragraph.SpaceAfter,
                                    paragraph.LineSpacingRule,
                                    paragraph.LineSpacing,
                                    paragraph.WidowControl,
                                    paragraph.KeepWithNext,
                                    paragraph.KeepTogether,
                                    paragraph.PageBreakBefore,
                                    paragraph.FarEastLineBreakControl,
                                    paragraph.WordWrap,
                                    paragraph.HangingPunctuation,
                                    paragraph.HalfWidthPunctuationOnTopOfLine,
                                    paragraph.AddSpaceBetweenFarEastAndAlpha,
                                    paragraph.BaseLineAlignment,]
            # print paragraph_properties
            hashed_paragraph_properties = ";".join([str(i) for i in paragraph_properties])
            paragraph_property_set.add(hashed_paragraph_properties)

            for sentence in app.Selection.Sentences:
                sentence_properties = [sentence.Font.Name,
                                       sentence.Font.NameAscii,
                                       sentence.Font.NameBi,
                                       sentence.Font.BoldBi,
                                       sentence.Font.ItalicBi,
                                       sentence.Font.SizeBi,
                                       sentence.Font.Bold,
                                       sentence.Font.Italic,
                                       sentence.Font.Size,
                                       sentence.Font.Underline,
                                       sentence.Font.EmphasisMark,
                                       sentence.Font.StrikeThrough,
                                       sentence.Font.DoubleStrikeThrough,
                                       sentence.Font.Superscript,
                                       sentence.Font.Subscript,
                                       sentence.Font.SmallCaps,
                                       sentence.Font.AllCaps,
                                       sentence.Font.Hidden,
                                       sentence.Font.Scaling,
                                       sentence.Font.Spacing,
                                       sentence.Font.Position,]
                # print sentence_properties
                hashed_sentence_properties = ";".join([str(i) for i in sentence_properties])
                sentence_property_set.add(hashed_sentence_properties)

        sentence_property_homogeneity = 1 if len(sentence_property_set) == 1 else 0
        paragraph_property_homogeneity = 1 if len(paragraph_property_set) == 1 else 0
        paragraph_count = len(range_list)
        biased_paragraph_kinds = len(paragraph_property_set) - 1

        return sentence_property_homogeneity, \
               paragraph_property_homogeneity, \
               paragraph_count, \
               biased_paragraph_kinds


    def save_result(self, range_list_of_level, doc_name, result_file_path):
        import codecs
        f = codecs.open(result_file_path, 'w', 'utf_8_sig')

        for (k, v) in range_list_of_level.items():
            style_id = k[0]
            level = k[1]
            sentence_property_homogeneity, paragraph_property_homogeneity, paragraph_count, biased_paragraph_kinds = \
                self.parse_ranges(v)
            r = "|".join(map(str, [doc_name,
                                 style_id,
                                 level,
                                 sentence_property_homogeneity,
                                 paragraph_property_homogeneity,
                                 paragraph_count,
                                 biased_paragraph_kinds,]))
            f.write(r + '\n')

        f.close()
