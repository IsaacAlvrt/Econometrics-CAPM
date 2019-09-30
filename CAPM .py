from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import pandas as pd

#Excel Workfile
wb = pd.read_excel("Tabla_6_1.xlsx")

#dataframe
df = pd.DataFrame({
    "X": wb["X"],
    "Y": wb["Y"]
})

#Linear regression without intercept
lm = ols("Y ~ X -1", df).fit()
print(lm.summary())

#t-test
t = lm.t_test("X = 1")
print(t)

#plot (without intercept)
plt.scatter(wb["X"], wb["Y"], color = "red")
plt.plot(wb["X"], 1.1555*wb["X"], color = "black")
plt.title("CAPM (without intercept)")
plt.xlabel("Systematic Risk")
plt.ylabel("Asset Risk")
plt.axis([-20, 20, -20, 20])
plt.grid()
plt.show()


#linear regression with intercept
lm2 = ols("Y ~ X", df).fit()
print(lm2.summary())

#plot (with intercept)
plt.scatter(wb["X"], wb["Y"], color = "red")
plt.plot(wb["X"], 1.1711*wb["X"] -0.4475, color = "black")
plt.title("CAPM (with intercept)")
plt.xlabel("Systematic Risk")
plt.ylabel("Asset Risk")
plt.axis([-20, 20, -20, 20])
plt.grid()
plt.show()
