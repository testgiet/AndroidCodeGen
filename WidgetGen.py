import re

wl = open("widgets.txt").read().splitlines()

declaration = []
inilization = []
fragment = []
adapter = []
viewholder = []
all = []

for w in wl:
    pos = re.search("Button|TextView|Linear|Relative|ImageView|listView|EditText|GridView", w).start()
    type = w[pos:]
    declaration.append("private {0} {1};".format(type, w))
    inilization.append("{0} = ({1}) findViewById(R.id.{0});".format(w, type))
    fragment.append("{0} = ({1}) view.findViewById(R.id.{0});".format(w, type))
    adapter.append("{1} {0} = ({1}) convertView.findViewById(R.id.{0});".format(w, type))
    viewholder.append("holder.{0} = ({1}) convertView.findViewById(R.id.{0});".format(w, type))
    all.append("{1} {0} = ({1}) findViewById(R.id.{0});".format(w, type))

print("\ndeclaration:")
for i in declaration:
    print(i)

print("\nactivity:")
for i in inilization:
    print(i)

print("\nfragment:")
for i in fragment:
    print(i)

print("\nadater: ")
for i in adapter:
    print(i)

print("\nview holder: ")
for i in viewholder:
    print(i)

print("\nall")
for i in all:
    print(i)

