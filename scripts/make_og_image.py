from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630

INK = (27, 36, 48)
INK_SOFT = (75, 85, 99)
PAPER = (241, 239, 230)
PAPER_2 = (230, 226, 212)
LINE = (201, 194, 172)
RUST = (174, 74, 36)
STEEL = (46, 83, 121)

FONT_DIR = r"C:\Windows\Fonts"
serif_bold = ImageFont.truetype(FONT_DIR + r"\HANBatangB.ttf", 92)
sans_reg = ImageFont.truetype(FONT_DIR + r"\malgun.ttf", 34)
sans_bold = ImageFont.truetype(FONT_DIR + r"\malgunbd.ttf", 30)
mono_reg = ImageFont.truetype(FONT_DIR + r"\consola.ttf", 26)
mono_small = ImageFont.truetype(FONT_DIR + r"\consola.ttf", 22)
stat_num = ImageFont.truetype(FONT_DIR + r"\malgunbd.ttf", 30)
stat_label = ImageFont.truetype(FONT_DIR + r"\malgun.ttf", 22)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# outer border
d.rectangle([0, 0, W - 1, H - 1], outline=LINE, width=2)

PAD_X = 90

# eyebrow: small rust tick + mono uppercase label
eyebrow_y = 84
d.line([(PAD_X, eyebrow_y), (PAD_X + 26, eyebrow_y)], fill=RUST, width=2)
d.text((PAD_X + 40, eyebrow_y - 14), "BACKEND ENGINEER PORTFOLIO", font=mono_small, fill=RUST)

# name
name_y = 150
d.text((PAD_X, name_y), "이정후", font=serif_bold, fill=INK)

# tagline, wrapped
tagline = "웹 아키텍처부터 AI 파이프라인까지, 데이터의 가치를 극대화하는 백엔드 엔지니어"


def wrap_text(text, font, max_width):
    lines = []
    current = ""
    for ch in text:
        test = current + ch
        if d.textlength(test, font=font) > max_width and current:
            lines.append(current)
            current = ch
        else:
            current = test
    if current:
        lines.append(current)
    return lines


max_w = W - PAD_X * 2
lines = wrap_text(tagline, sans_reg, max_w)

ty = 300
for line in lines:
    d.text((PAD_X, ty), line, font=sans_reg, fill=INK_SOFT)
    ty += 48

# bottom divider
div_y = 470
d.line([(PAD_X, div_y), (W - PAD_X, div_y)], fill=LINE, width=1)

# bottom stat-like row: 3 highlights
stats = [
    ("4년", "LG유플러스 · LG CNS SI/SM"),
    ("MSA", "레거시 모놀리식 전환"),
    ("LLM", "실시간 데이터 파이프라인"),
]
col_w = (W - PAD_X * 2) / 3
sy = div_y + 34
for i, (num, label) in enumerate(stats):
    x = PAD_X + i * col_w
    d.text((x, sy), num, font=stat_num, fill=RUST)
    d.text((x, sy + 40), label, font=stat_label, fill=INK_SOFT)

img.save(r"C:\dev\junghoo-dev\images\og-image.png")
print("saved")
