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
                if range_[1] - range_[0] >= 2:
                    range_ = (range_[0]+1, range_[1]-1)

                app.Selection.SetRange(range_[0], range_[1])

                paragraph = app.Selection.Paragraphs(1)
                paragraph_properties = [paragraph.TabStops.Count,                    # 制表位个数
                                        paragraph.TabStops(1).Position,              # 制表位位置
                                        paragraph.TabStops(1).Alignment,             # 制表位对齐方式
                                        paragraph.TabStops(1).Leader,                # 制表位前导符
                                        paragraph.Alignment,                         # 对齐方式
                                        paragraph.OutlineLevel,                      # 大纲级别
                                        paragraph.ReadingOrder,                      # 方向
                                        paragraph.CharacterUnitLeftIndent,           # 左缩进
                                        paragraph.CharacterUnitRightIndent,          # 右缩进
                                        paragraph.LeftIndent,                        # 文本之前（后）
                                        paragraph.CharacterUnitFirstLineIndent,      # 首行缩进
                                        paragraph.FirstLineIndent,                   # 首行缩进
                                        paragraph.LineUnitBefore,                    # 段前间距
                                        paragraph.SpaceBefore,                       # 段前间距
                                        paragraph.LineUnitAfter,                     # 段后间距
                                        paragraph.SpaceAfter,                        # 段后间距
                                        paragraph.LineSpacingRule,                   # 行距
                                        paragraph.LineSpacing,                       # 行距
                                        paragraph.WidowControl,                      # 孤行控制
                                        paragraph.KeepWithNext,                      # 与下段同页
                                        paragraph.KeepTogether,                      # 段中不分页
                                        paragraph.PageBreakBefore,                   # 分页
                                        paragraph.FarEastLineBreakControl,           # 按中文习惯控制首尾字符
                                        paragraph.WordWrap,                          # 允许西文在单词中间换行
                                        paragraph.HangingPunctuation,                # 允许标点溢出边界
                                        paragraph.HalfWidthPunctuationOnTopOfLine,   # 允许行首标点压缩
                                        paragraph.AddSpaceBetweenFarEastAndAlpha,    # 自动调整中文和西文的间距
                                        paragraph.BaseLineAlignment, ]               # 文本对齐方式
                para_text = paragraph.Range.Text
                self.raw_para_data[k].append((para_text.replace('\r', '').replace('\n', ''), paragraph_properties))

                # print k, range_

                for sentence in app.Selection.Sentences:
                    sentence_properties = [sentence.Font.Name,                       # 中文字体
                                           sentence.Font.NameAscii,                  # 西文字体
                                           sentence.Font.NameBi,                     # 复杂文种
                                           sentence.Font.BoldBi,                     # 复杂文种-粗体
                                           sentence.Font.ItalicBi,                   # 复杂文种-斜体
                                           sentence.Font.SizeBi,                     # 复杂文种-字号
                                           sentence.Font.Bold,                       # 粗体
                                           sentence.Font.Italic,                     # 斜体
                                           sentence.Font.Size,                       # 字号
                                           sentence.Font.Underline,                  # 下划线
                                           sentence.Font.EmphasisMark,               # 着重号
                                           sentence.Font.StrikeThrough,              # 删除线
                                           sentence.Font.DoubleStrikeThrough,        # 双删除线
                                           sentence.Font.Superscript,                # 上标
                                           sentence.Font.Subscript,                  # 下标
                                           sentence.Font.SmallCaps,                  # 小型大写字母
                                           sentence.Font.AllCaps,                    # 全部大写字符
                                           sentence.Font.Hidden,                     # 隐藏文字
                                           sentence.Font.Scaling,                    # 字符间距-缩放
                                           sentence.Font.Spacing,                    # 字符间距-间距
                                           sentence.Font.Position, ]                 # 字符间距-位置
                    sent_text = sentence.Text
                    self.raw_sentence_data[k].append((sent_text.replace('\r', '').replace('\n', ''), sentence_properties))
                    # print sent_text.replace('\r', '').replace('\n', '')
