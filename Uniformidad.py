import random
import math

def prueba_chi_cuadrada():
    print("=" * 65)
    print("        PRUEBA DE UNIFORMIDAD - CHI CUADRADA")
    print("=" * 65)
    n = int(input("\nIngresa el número de números aleatorios (n): "))
    numeros = [random.random() for _ in range(n)]
    k = math.ceil(1 + 3.322 * math.log10(n))
    alpha = 0.05
    print("\n--- NÚMEROS ALEATORIOS GENERADOS ---")
    for i, numero in enumerate(numeros, start=1):
        print(f"{i:3}. {numero:.6f}")
    ancho_intervalo = 1.0 / k
    frecuencias = [0] * k
    for numero in numeros:
        indice = int(numero / ancho_intervalo)
        if indice >= k:
            indice = k - 1
        frecuencias[indice] += 1
    Ei = n / k
    print("\n" + "=" * 65)
    print("              DATOS DE LA PRUEBA")
    print("=" * 65)
    print(f"Número de datos (n):          {n}")
    print(f"Número de intervalos (k):    {k}")
    print(f"Nivel de significancia (α):  {alpha}")
    print(f"Frecuencia esperada (Ei):    {Ei:.4f}")
    print("\n--- RESULTADOS POR INTERVALO ---")
    print(
        f"{'Intervalo':<12}"
        f"{'Límites':<18}"
        f"{'Oi':<10}"
        f"{'Ei':<10}"
        f"{'Chi² parcial':<15}"
    )
    print("-" * 65)
    suma_chi2 = 0.0
    for i in range(k):
        lim_inf = i * ancho_intervalo
        lim_sup = (i + 1) * ancho_intervalo
        Oi = frecuencias[i]
        chi2_parcial = ((Oi - Ei) ** 2) / Ei
        suma_chi2 += chi2_parcial
        if i == k - 1:
            limites = f"[{lim_inf:.3f} - {lim_sup:.3f}]"
        else:
            limites = f"[{lim_inf:.3f} - {lim_sup:.3f})"
        print(
            f"{i + 1:<12}"
            f"{limites:<18}"
            f"{Oi:<10}"
            f"{Ei:<10.2f}"
            f"{chi2_parcial:<15.4f}"
        )
    print("-" * 65)
    print(f"\nEstadístico calculado Chi² = {suma_chi2:.4f}")
    gl = k - 1
    print(f"Grados de libertad (gl) = {gl}")
    tabla_chi2 = {
        1: 3.841,
        2: 5.991,
        3: 7.815,
        4: 9.488,
        5: 11.070,
        6: 12.592,
        7: 14.067,
        8: 15.507,
        9: 16.919,
        10: 18.307,
        11: 19.675,
        12: 21.026,
        13: 22.362,
        14: 23.685,
        15: 24.996,
        16: 26.296,
        17: 27.587,
        18: 28.869
    }
    if gl in tabla_chi2:
        chi2_tabla = tabla_chi2[gl]
        print("\n" + "=" * 65)
        print("                    CONCLUSIÓN")
        print("=" * 65)
        print(f"Chi² calculada = {suma_chi2:.4f}")
        print(f"Chi² crítica   = {chi2_tabla:.4f}")
        print(f"α              = {alpha}")
        print(f"gl             = {gl}")
        print("\nHipótesis:")
        print("H₀: Los números siguen una distribución uniforme.")
        print("H₁: Los números NO siguen una distribución uniforme.")
        print("\nComparación:")
        if suma_chi2 < chi2_tabla:
            print(
                f"{suma_chi2:.4f} < {chi2_tabla:.4f}"
            )
            print("\nDECISIÓN: NO SE RECHAZA H₀.")
            print(
                "Conclusión: Los números generados son compatibles "
                "con una distribución uniforme."
            )
        else:
            print(
                f"{suma_chi2:.4f} >= {chi2_tabla:.4f}"
            )
            print("\nDECISIÓN: SE RECHAZA H₀.")
            print(
                "Conclusión: Los números generados NO son compatibles "
                "con una distribución uniforme."
            )
    else:
        print("\nNo existe el valor crítico en la tabla para")
        print(f"los grados de libertad: {gl}")
        print(
            "Puedes ampliar la tabla de valores críticos "
            "si necesitas trabajar con un número mayor de intervalos."
        )
    print("\n" + "=" * 65)
    print("                  FIN DEL PROGRAMA")
    print("=" * 65)
if __name__ == "__main__":
    prueba_chi_cuadrada()
