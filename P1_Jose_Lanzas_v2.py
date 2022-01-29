import pandas as pd
import numpy as np

#APARTADO 2
try:
    # Leemos el archivo
    frame_data = pd.read_csv('finanzas2020[1].csv',sep='\t')
    df = pd.DataFrame(frame_data)

    # Comprobamos que todo es correcto
    A = ('Enero' and 'Febrero' and 'Marzo' and 'Abril' and 'Mayo' and 'Junio' and 'Julio' and 'Agosto' and 'Septiembre' and 'Octubre' and 'Noviembre' and 'Diciembre') in df.columns
    B = df.Enero.empty and df.Febrero.empty and df.Marzo.empty and df.Abril.empty and df.Mayo.empty and df.Junio.empty and df.Julio.empty and df.Agosto.empty and df.Septiembre.empty and df.Octubre.empty and df.Noviembre.empty and df.Diciembre.empty

    if (A==True and B==False):
        print("\nEl archivo finanzas se ha leído correctamente, tiene 12 columnas con contenido, una para cada mes del año \n ")

        # Corregimos los datos dañados
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


            gastos_mes = [g_1, g_2, g_3, g_4, g_5, g_6, g_7, g_8, g_9, g_10, g_11, g_12]
            neto_mes = [n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, n_10, n_11, n_12]


            leyenda = pd.DataFrame({"Posicion": ["1", "2", "3", "4", "5","6","7","8","9","10","11","12"], "Mes": ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]})


            # DEFINIMOS LAS FUNCIONES

            # ¿Qué mes se ha gastado más?
            def peor_mes(gastos_mes):
                mes_gastoso = min(gastos_mes)
                for i in range(len(gastos_mes)):
                    if mes_gastoso == gastos_mes[i]:
                        return leyenda.iloc[i]["Mes"]


            # ¿Cuál ha sido el gasto total a lo largo del año?
            def gasto_total(df):
                gasto= 0
                for i in range(len(df.index)):
                    for j in range(len(df.columns)):
                        if df.iloc[i,j] < 0:
                            gasto += df.iloc[i,j]
                return gasto


            # ¿Cuál es la media de gastos del año?
            def media_gastos(df):
                g = 0
                for i in range(len(df.index)):
                    for j in range(len(df.columns)):
                        if df.iloc[i,j] < 0:
                            g += 1
                return gasto_total(df)/g


            # ¿Qué mes se ha ahorrado más?
            def mejor_mes(neto_mes):
                mes_ahorrador = max(neto_mes)
                for i in range(len(neto_mes)):
                    if mes_ahorrador == neto_mes[i]:
                        return leyenda.iloc[i]["Mes"]


            # ¿Cuál ha sido el ingreso total a lo largo del año?
            def ingreso_total(df):
                ingreso = 0
                for i in range(len(df.index)):
                    for j in range(len(df.columns)):
                        if df.iloc[i,j] > 0:
                            ingreso += df.iloc[i,j]
                return ingreso


            # LLAMAMOS A LOS RESULTADOS
            print('El mes que más se gastó fue', peor_mes(gastos_mes), "\n")
            print('El gasto total a lo largo del año es de', gasto_total(df), '€ \n')
            print('La media de gastos del año es de', media_gastos(df),'€ \n')
            print('El mes que más se ahorró fue', mejor_mes(neto_mes),'\n')
            print('El ingreso total a lo largo del año es de', ingreso_total(df),'€ \n')


        except:
            print("Hay datos del archivo que no pueden corregirse \n")

    else:
        print("\nEl archivo finanzas NO se ha leído correctamente, compruebe que tiene 12 columnas con contenido, una por cada mes del año \n")

except:
    print("\nEl archivo finanzas NO se ha leído correctamente, compruebe que el archivo existe \n")

