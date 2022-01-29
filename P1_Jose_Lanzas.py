import pandas as pd
import numpy as np

#APARTADO 2
try:
    frame_data = pd.read_csv('finanzas2020[1].csv',sep='\t')
    df = pd.DataFrame(frame_data)
    A = ('Enero' and 'Febrero' and 'Marzo' and 'Abril' and 'Mayo' and 'Junio' and 'Julio' and 'Agosto' and 'Septiembre' and 'Octubre' and 'Noviembre' and 'Diciembre') in df.columns
    B = df.Enero.empty and df.Febrero.empty and df.Marzo.empty and df.Abril.empty and df.Mayo.empty and df.Junio.empty and df.Julio.empty and df.Agosto.empty and df.Septiembre.empty and df.Octubre.empty and df.Noviembre.empty and df.Diciembre.empty
    if (A==True and B==False): 
        print("\nEl archivo finanzas se ha leído correctamente, tiene 12 columnas con contenido, una para cada mes del año \n ")

        try:
            cont=0
            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    if type(df.iloc[i,j]) == str:
                        cont += 1
                        try:
                            df.iloc[i,j] = float(df.iloc[i,j])
                        except:
                            df.iloc[i,j] = 0
                        else:
                            cont -= 1

            print(f"Hay un total de {cont} datos dañados que han sido corregidos \n")

            # APARTADO 1
            # Gastos de cada mes
            g_1 = float(df.loc[df['Enero'] < 0, ['Enero']].sum())
            g_2 = float(df.loc[df['Febrero'] < 0, ['Febrero']].sum())
            g_3 = float(df.loc[df['Marzo'] < 0, ['Marzo']].sum())
            g_4 = float(df.loc[df['Abril'] < 0, ['Abril']].sum())
            g_5 = float(df.loc[df['Mayo'] < 0, ['Mayo']].sum())
            g_6 = float(df.loc[df['Junio'] < 0, ['Junio']].sum())
            g_7 = float(df.loc[df['Julio'] < 0, ['Julio']].sum())
            g_8 = float(df.loc[df['Agosto'] < 0, ['Agosto']].sum())
            g_9 = float(df.loc[df['Septiembre'] < 0, ['Septiembre']].sum())
            g_10 = float(df.loc[df['Octubre'] < 0, ['Octubre']].sum())
            g_11 = float(df.loc[df['Noviembre'] < 0, ['Noviembre']].sum())
            g_12 = float(df.loc[df['Diciembre'] < 0, ['Diciembre']].sum())

            # Valor neto de cada mes
            n_1 = float(df.Enero.sum())
            n_2 = float(df.Febrero.sum())
            n_3 = float(df.Marzo.sum())
            n_4 = float(df.Abril.sum())
            n_5 = float(df.Mayo.sum())
            n_6 = float(df.Junio.sum())
            n_7 = float(df.Julio.sum())
            n_8 = float(df.Agosto.sum())
            n_9 = float(df.Septiembre.sum())
            n_10 = float(df.Octubre.sum())
            n_11 = float(df.Noviembre.sum())
            n_12 = float(df.Diciembre.sum())

            # Ingresos de cada mes
            e_1 = float(df.loc[df['Enero'] > 0, ['Enero']].sum())
            e_2 = float(df.loc[df['Febrero'] > 0, ['Febrero']].sum())
            e_3 = float(df.loc[df['Marzo'] > 0, ['Marzo']].sum())
            e_4 = float(df.loc[df['Abril'] > 0, ['Abril']].sum())
            e_5 = float(df.loc[df['Mayo'] > 0, ['Mayo']].sum())
            e_6 = float(df.loc[df['Junio'] > 0, ['Junio']].sum())
            e_7 = float(df.loc[df['Julio'] > 0, ['Julio']].sum())
            e_8 = float(df.loc[df['Agosto'] > 0, ['Agosto']].sum())
            e_9 = float(df.loc[df['Septiembre'] > 0, ['Septiembre']].sum())
            e_10 = float(df.loc[df['Octubre'] > 0, ['Octubre']].sum())
            e_11 = float(df.loc[df['Noviembre'] > 0, ['Noviembre']].sum())
            e_12 = float(df.loc[df['Diciembre'] > 0, ['Diciembre']].sum())

            leyenda = pd.DataFrame({"Posicion": ["1", "2", "3", "4", "5","6","7","8","9","10","11","12"], "Mes": ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]})


            # ¿Qué mes se ha gastado más?
            gastos_mes = [g_1, g_2, g_3, g_4, g_5, g_6, g_7, g_8, g_9, g_10, g_11, g_12]
            mes_gastoso = min(gastos_mes)
            for i in range(len(gastos_mes)):
                if mes_gastoso == gastos_mes[i]:
                    print(f'El mes que más se gastó fue  {leyenda.iloc[i]["Mes"]} \n')


            # ¿Cuál ha sido el gasto total a lo largo del año?
            gasto_total = 0
            for i in range(len(gastos_mes)):
                gasto_total += gastos_mes[i]

            print(f'El gasto total a lo largo del año es de {gasto_total} € \n')


            # ¿Cuál es la media de gastos del año?
            g = 0
            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    if df.iloc[i,j] < 0:
                        g += 1

            print(f'La media de gastos del año es de {gasto_total/g} € \n')


            # ¿Qué mes se ha ahorrado más?
            neto_mes = [n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, n_10, n_11, n_12]
            mes_ahorrador = max(neto_mes)
            for i in range(len(neto_mes)):
                if mes_ahorrador == neto_mes[i]:
                    print(f'El mes que más se ahorró fue {leyenda.iloc[i]["Mes"]} \n')


            # ¿Cuál ha sido el ingreso total a lo largo del año?
            ingresos_mes = [e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8, e_9, e_10, e_11, e_12]
            ingreso_total = 0
            for i in range(len(ingresos_mes)):
                ingreso_total += ingresos_mes[i]

            print(f'El ingreso total a lo largo del año es de {ingreso_total} € \n')


        except:
            print("Hay datos del archivo que no pueden corregirse \n")

    else:
        print("\nEl archivo finanzas NO se ha leído correctamente, compruebe que tiene 12 columnas con contenido, una para cada mes del año \n")

except:
    print("\nEl archivo finanzas NO se ha leído correctamente, compruebe que el archivo existe \n")
