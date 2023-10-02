#!/usr/bin/wish

pack [label .l1 -text "Package Name:"]
pack [entry .e1]

pack [label .l2 -text "Description:"]
pack [text .t2 -height 4 -width 50]

pack [label .l3 -text "Associated Nodes:"]
pack [entry .e3]

pack [label .l4 -text "Associated Files:"]
pack [entry .e4]

pack [button .b1 -text "Add Package" -command {exec python3 app.py}]
pack [label .status -text ""]

bind . <Return> {exec python3 app.py}