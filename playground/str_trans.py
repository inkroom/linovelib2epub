mapping_dict = {
    '“': "「",
    '’': "』",
    "": "是",
    "": "不",
    "": "他",
    "": "个",
    "": "来",
    "": "大",
    "": "子",
    "": "说",
    "": "年",
    "": "那",
    "": "她",
    "": "得",
    "": "自",
    "": "家",
    "": "而",
    "": "去",
    "": "小",
    "": "于",
    "": "么",
    "": "好",
    "": "发",
    "": "成",
    "": "事",
    "": "用",
    "": "道",
    "": "种",
    "": "乳",
    "": "茎",
    "": "肉",
    "": "胸",
    "": "淫",
    "": "射",
    "": "骚",
    '”': "」",
    "": "的",
    "": "了",
    "": "人",
    "": "有",
    "": "上",
    "": "到",
    "": "地",
    "": "中",
    "": "生",
    "": "着",
    "": "和",
    "": "出",
    "": "里",
    "": "以",
    "": "可",
    "": "过",
    "": "能",
    "": "多",
    "": "心",
    "": "之",
    "": "看",
    "": "当",
    "": "只",
    "": "把",
    "": "第",
    "": "想",
    "": "开",
    "": "阴",
    "": "欲",
    "": "交",
    "": "私",
    "": "臀",
    "": "脱",
    "": "唇",
    '‘': "『",
    "": "一",
    "": "我",
    "": "在",
    "": "这",
    "": "们",
    "": "时",
    "": "为",
    "": "你",
    "": "国",
    "": "就",
    "": "要",
    "": "也",
    "": "后",
    "": "会",
    "": "下",
    "": "天",
    "": "对",
    "": "然",
    "": "学",
    "": "都",
    "": "起",
    "": "没",
    "": "如",
    "": "还",
    "": "样",
    "": "作",
    "": "美",
    "": "液",
    "": "呻",
    "": "性",
    "": "穴",
    "": "舔",
    "": "裸",
}

table = str.maketrans(mapping_dict)
txt = "abb"
res = txt.translate(table)
print(res)