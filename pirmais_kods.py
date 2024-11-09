kods?


print("Izvēlieties (nospiediet ttiecīgo ciparu): ")
print("[1-Taisnstūris, 2 - trīsstūris]")
figura = int(input("Jūsu izvēle: "))
match figura:
    case 1:
        mala_a=float(input("Ievadiet taisnstūra a malas garumu (cm): "))
        mala_b=float(input("Ievadiet taisnstūra mals garumu (cm): "))
        perimetrs = 2*(mala_a +mala_b)
        print (f"Taisnstūra perimetrs ir {perimetrs:2f} cm")
    case 2:
        mala_a=float(input("Ievadiet tristura a malas garumu (cm): "))
        mala_b=float(input("Ievadiet tristura b malas garumu (cm): "))
        mala_c=float(input("Ievadiet tristura c malas garumu (cm): "))
        perimetrs = (mala_a +mala_b+mala_c)
        print (f"Taisnstūra perimetrs ir {perimetrs:2f} cm")
    case _: 
            print("Tādas figūras nav.")
