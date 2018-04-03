Button_Colours = {"PureTec":"red", "ChemTec":"blue", "LabTec":"green", "MabTec":"brown", "FilterTec":"purple", "FilterTecPlus":"purple"}

Pumps = list(dict.keys(Button_Colours))

for a in range (0, len(Pumps)):
  vars()["btn_"+Pumps[a]] = [Pumps[a], Button_Colours[Pumps[a]]]

print(btn_PureTec)
print(btn_ChemTec)
print(btn_LabTec)
print(btn_MabTec)
print(btn_FilterTec)
print(btn_FilterTecPlus)
