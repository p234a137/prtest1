
import pandas as pd
import numpy as np
import matplotlib.pylab as pl


from sklearn.datasets import load_boston

import re


if __name__ == "__main__":
  boston = load_boston()

  def camel_to_snake(column_name):
      """
      converts a string that is camelCase into snake_case
      Example:
          print camel_to_snake("javaLovesCamelCase")
          > java_loves_camel_case
      """
      s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
      return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

  df = pd.DataFrame(boston.data)

  df.columns = [camel_to_snake(col) for col in boston.feature_names[:]]


  # add in prices
  df['price'] = boston.target

  from sklearn.linear_model import LinearRegression

  features = ['age', 'lstat', 'tax']
  lm = LinearRegression()
  lm.fit(df[features], df.price)
  print df.price[1:10]
  print lm.predict(df[features])[1:10]

  # add your actual vs. predicted points
  pl.scatter(df.price, lm.predict(df[features]))
  # add the line of perfect fit
  straight_line = np.arange(0, 60)
  pl.plot(straight_line, straight_line)
  pl.title("Fitted Values")
