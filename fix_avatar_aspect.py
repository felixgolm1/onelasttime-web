import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Using regex to find the drawImage block
pattern = re.compile(r'ctx\.clip\(\);\s*ctx\.drawImage\(chatAvatar,\s*avatarX,\s*avatarY,\s*avatarSize,\s*avatarSize\);\s*ctx\.restore\(\);')

new_code = '''ctx.clip();
                let scale = Math.max(avatarSize / chatAvatar.naturalWidth, avatarSize / chatAvatar.naturalHeight);
                let drawW = chatAvatar.naturalWidth * scale;
                let drawH = chatAvatar.naturalHeight * scale;
                let drawX = avatarX + (avatarSize - drawW) / 2;
                let drawY = avatarY + (avatarSize - drawH) / 2;
                ctx.drawImage(chatAvatar, drawX, drawY, drawW, drawH);
                ctx.restore();'''

content = pattern.sub(new_code, content)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
