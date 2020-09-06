replacer = {
  '<s>': r'\(^\|[^HANGEUL]\)',
  '<_>': r'\(\n\|[^HANGEUL]\)',

  'NUM_*': r'NUMNUM_+',
  'NUM_+': r'NUM_IEUNGNUM_HIEUH',
  '*_NUM': r'+_NUMNUM',
  '+_NUM': r'IEUNG_NUMHIEUH_NUM',
  'IEUNG_*': r'IEUNGIEUNG_+',
  'IEUNG_+': r'IEUNG_NUMIEUNG_HIEUH',
  '*_IEUNG': r'IEUNGNUM_IEUNG',
  'HIEUH_*': r'HIEUHHIEUH_NUM',
  '*_HIEUH': r'+_HIEUHHIEUH',
  '+_HIEUH': r'NUM_HIEUHIEUNG_HIEUH',

  'NUM_IEUNG': r'\u1135\u114D',
  'IEUNG_NUM': r'\u1141-\u1146\u1148-\u114B\u3182\u3183\uA976',
  'IEUNG_HIEUH': r'\uA977',
  'NUM_HIEUH': r'\u111A\u113B\u1153\u115Dㄶㅀ\uA974\uA97Aﾦﾰ',
  'HIEUH_NUM': r'\uA97B',

  'KIYEOK': r'\u1100\u1101\u110Fㄱㄲㅋ가-낗카-킿ﾡﾢﾻ',
  'NIEUN': r'\u1102\u1114ㄴ\u3165나-닣ﾤ',
  'TIKEUT': r'\u1103\u1104\u1110\uA979ㄷㄸㅌ다-띻타-팋ﾧﾨﾼ',
  'RIEUL': r'\u1105\u1119\u111Bㄹ라-맇ﾩ',
  'MIEUM': r'\u1106\u111Dㅁ\u3171마-밓ﾱ',
  'PIEUP': r'\u1107\u1108\u1111\u112B\u112C\u1157ㅂㅃㅍ\u3178\u3179\u84바-삫파-핗ﾲﾳﾽ',
  'SIOS': r'\u1109\u110A\u113C-\u1140ㅅㅆ사-앃ﾵﾶ',
  'IEUNG': r'\u110B\u1147\u114Cㅇ\u3180\u3181아-잏ﾷ',
  'CIEUC': r'\u110C-\u110E\u114E-\u1151\u1154\u1155ㅈ-ㅊ자-칳ﾸ-ﾺ',
  'HIEUH': r'\u1112\u1158\u1159ㅎ\u3185\u3186\uA97C하-힣ﾾ',

  'NUMETC': r'\u1100-\u110A\u110C-\u1111\u1113-\u1119\u111B-\u1134\u1136-\u113A\u113C-\u1140\u114E-\u1152\u1154-\u1157\u115A-\u115C\u115E-\u11FF\u302E\u302Fㄱ-ㄵㄷ-ㄿㅁ-ㅆㅈ-ㅍㅏ-\u316C\u316E-\u317F\u3184\u3187-\u318E\uA960-\uA973\uA975\uA979가-앃자-핗\uD7B0-\uD7C6\uD7CB-\uD7FB\uFFA0-ﾥﾧ-ﾯﾱ-ﾶﾸ-ﾽￂ-ￇￊ-ￏￒ-ￗￚ-ￜ',
  'NUM': r'\u1100-\u110A\u110C-\u1111\u1113-\u1119\u111B-\u1134\u1136-\u113A\u113C-\u1140\u114E-\u1152\u1154-\u1157\u115A-\u115C\u115Eㄱ-ㄵㄷ-ㄿㅁ-ㅆㅈ-ㅍ\u3165-\u316C\u316E-\u317F\u3184\uA960-\uA973\uA975\uA979가-앃자-핗ﾡ-ﾥﾧ-ﾯﾱ-ﾶﾸ-ﾽ',
  'ETC': r'\u1160-\u11FF\u302E\u302Fㅏ-\u3164\u3187-\u318E\uD7B0-\uD7C6\uD7CB-\uD7FB\uFFA0ￂ-ￇￊ-ￏￒ-ￗￚ-ￜ',
  'HANGEUL': r'\u1100-\u11FF\u302E\u302F\u3131-\u318E가-힣\uA960-\uA97C\uD7B0-\uD7C6\uD7CB-\uD7FB\uFFA0-\uFFBEￂ-ￇￊ-ￏￒ-ￗￚ-ￜ',
}

with open('pbhhg.src.vim', 'r') as f:
  src = f.read()

dest = src
for k, v in replacer.items():
  dest = dest.replace(k, v)

with open('syntax/pbhhg.vim', 'w') as f:
  f.write(dest)

