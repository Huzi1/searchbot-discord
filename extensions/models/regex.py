# WARNING This list includes slurs.

from re import compile, I, X

nono_re = compile(
r"""tranny|
faggot|
fag\b|
\bporn|
\bcock\b|
dick|
t\s*i\s*t\s*t\s*y|
\bt\s*i\s*t\b|
\bb\s*o\s*o\s*b|
p\s*e\s*n\s*i\s*s|
s\s*l\s*u\s*t|
\bc\s*u\s*m\b|
\bj\s*i\s*z\s*z|
\bsemen\b|
[cg]ooch|
pussy|
penis|
fetish|
bdsm|
sexy|
xxx|
orgasm|
masturbat|
erotic|
creampie|
fap|
\bnude\b|
orgasm|
squirting|
y\s*i\s*f\s*f|
e\s*6\s*2\s*1|
\bsex|
ejaculat|
cunt| # scunthorpe
vagina|
coom|
troon|
h\s*e\s*n\s*t\s*a\s*i|
yaoi|
bukkake|
bara\b|
shota|
loli|
toddlercon|
fetish|
spunk|
pron|
p0rn|
pr0n|
gloryhole|
felch|
(skull|goat|dog)fuck|
\bscat\b|
piss\s*(play)?|
underage|
bbw|
fisting|
queef|
rimming|
rimjob|
bdsm|
cbt|
blumpkin|
boner|
prostitut|
butt\s*plug|
transvestite|
femboy|
castrat|
philia|
edging|
edgeplay|
enema|
facial|
fellat|
femdom|
(foot|blow|tit|hand)job|
frot|
gang\s*bang|
glory\s*hole|
hermap|
(jerk|jack)(ing)?\s*off|
kink|
wet\s*dream|
\banal\b| # banal, analyze
pegging|
pre(-?|\s*)cum|
priap|
scrotum|
shemale|
smegma|
smut|
softcore|
transs?exual|
voyeur|
viagra|
wank|
whore|
\bnigger| # not snigger
nignog|
watersports|
vietnamese\s*landmine|
dirty\s*sanchez|
\bass\b|
\bsh[ia]t\b|
\bpoo\b|
\brape\b|
\bjap\b|
\bspic\b|
chink|
retard|
\btard\b|
bitch|
\barse\b|
\banus\b|
blue\s*waffle|
tubgirl|
goatse|
\bt\s*r\s*a\s*n\s*n\s*y\b|
\bf\s*a\s*g\s*g\s*o\s*t\b|
\bt\s*i\s*t\s*t\s*y\b|
\bd\s*i\s*c\s*k\b|
\bb\s*u\s*k\s*k\s*a\s*k\s*e\b|
\bs\s*h\s*o\s*t\s*a\b|
\bl\s*o\s*l\s*i\b|
\bt\s*o\s*d\s*d\s*l\s*e\s*r\s*c\s*o\s*n\b|
\bf\s*e\s*t\s*i\s*s\s*h\b|
\bp\s*r\s*o\s*n\b|
\bp\s*0r\s*n\b|
\bp\s*r\s*0n\b|
\bg\s*l\s*o\s*r\s*y\s*h\s*o\s*l\s*e\b|
\b(s\s*k\s*u\s*l\s*l\s*|g\s*o\s*a\s*t\s*|d\s*o\s*g\s*)f\s*u\s*c\s*k\b|
\bu\s*n\s*d\s*e\s*r\s*a\s*g\s*e\b|
\bb\s*b\s*w\b|
\bb\s*l\s*u\s*m\s*p\s*k\s*i\s*n\b|
\bp\s*r\s*o\s*s\s*t\s*i\s*t\s*u\s*t\b|
\bb\s*u\s*t\s*t\s*p\s*l\s*u\s*g\b|
\bt\s*r\s*a\s*n\s*s\s*v\s*e\s*s\s*t\s*i\s*t\s*e\b|
\bf\s*e\s*m\s*b\s*o\s*y\b|
\bc\s*a\s*s\s*t\s*r\s*a\s*t\b|
\b(f\s*o\s*o\s*t\s*|b\s*l\s*o\s*w\s*|t\s*i\s*t\s*|h\s*a\s*n\s*d\s*)j\s*o\s*b\b|
\bs\s*c\s*r\s*o\s*t\s*u\s*m\b|
\bs\s*h\s*e\s*m\s*a\s*l\s*e\b|
\bs\s*m\s*e\s*g\s*m\s*a\b|
\d{6}""",
I | X
)


def setup(bot):
    pass
