def calculatorTip(tagihan = 0):
    tagihan = tagihan;
    tip = 0.15 * tagihan if tagihan >= 50 and tagihan <= 300 else 0.2 * tagihan
    total_akhir = tagihan+tip
    print("Tagihannya ",tagihan,","," tipnya ",tip,","," Total akhir ",total_akhir)

calculatorTip(275)
calculatorTip(40)
calculatorTip(430)
