An enhancement to pandas module.
This is kungfu, with monkey-patched common methods to (Data)Frame and Series in pandas.
jerryzhujian9_at_gmail.com
Tested under python 2.7.

Install:
https://pypi.python.org/pypi/kungfu
pip install kungfu
The above command will auto take care of the following requirements
Requires pandas 0.12.0 (tested 0.12.0-2) which will also install python-dateutil(dateutil), numpy, pytz, six
Requires openpyxl for writing excel (tested with 1.5.8, version 1.6.1 or higher, but lower than 2.0.0 may also work.)
xlrd for reading excel, xlwt for writing .xls (old format) file
(pip install pandas==0.12.0; pip install openpyxl==1.5.8; pip install xlrd; pip install xlwt)

Usage:
http://pandas.pydata.org/pandas-docs/version/0.12.0/genindex.html

Generally all of the calling (monkey-patched or not) returns something and the original frame or series remains unchanged.
If user wants the original frame or series to be changed, assign the returns back.

Visualize a series as a column of a frame with the series name being the column name.
Visualize a single list as a series and therefore a column of a frame when converting a series or frame.
However, for a list of lists, Visualize each list of the list (i.e. sublist) as a row!
Memorization: list=series=column

Frame.read(x) = Frame.Read(x)               Frame.save = Frame.Save                     Frame.write = Frame.Save
Frame.peek = Frame.Print                    Frame.Peek = Frame.Print                    Frame.play = Frame.Play
Frame.sel = Frame.Sel                       Frame.selcol = Frame.SelCol                 Frame.selrow = Frame.SelRow
Frame.delete/remove = Frame.Del             Frame.groupv = Frame.GroupV                 Frame.splith = Frame.SplitH
Frame.recols = Frame.ReorderCols            Frame.rerows = Frame.ReorderRows            Frame.rncols = Frame.RenameCols
Frame.newcol = Frame.NewCol                 Frame.findval = Frame.FindVal               Frame.countval = Frame.CountVal
Frame.cnames = Frame.Columns                Frame.names = Frame.Columns                 Frame.rnames = Frame.Indices
Frame.num = Frame.ToNum                     Frame.maskout = Frame.Maskout               # Frame.fillna = Frame.FillNA

Series.play = Series.Play                   Series.peek = Series.Print                  Series.Peek = Series.Print
Series.sel = Series.Sel                     Series.countval = Series.CountVal           # Series.unique = Series.Uniques  --existing method
Series.len = Series.Size                    Series.names = Series.Indices               Series.rnames = Series.Indices
Series.cames = Series.Indices               Series.num = Series.ToNum                   Series.str = Series.ToStr
Series.maskout = Series.Maskout             # Series.fillna = Series.FillNA

from pandas import isnull as isna
from pandas import isnull as isnull
frame.mean(axis=0),frame.median(axis=0),frame.sum(axis=0)
series.mean(axis=0),series.median(axis=0),series.sum(axis=0)
series.corr(other, method='')

mergelr = MergeLR                           concatvh = ConcatVH
Frame.tolist(), Frame.list()<--homebrew     Series.tolist(), Series.list()   <--exisiting method in pandas
General notes on "join":
    when joining along an axis, the index of each frame does not have to in the same order
    e.g. ["a","b","c","f"] for left frame, ["b","c","a","e"] for right frame
    join will match them and return the combined frame (in a certain order)

e.g., 
outputFrame = kf.MergeLR(outputFrame, tempFrame, join="inter", onKeys=[["sbj", "wordpair"]], sort=False)

tempFrame = kf.ConcatVH([tempFrame, immediate, delayed]) 
tempRow = [sbj, cnd, memoryTesting, memoryImmediate, memoryDelay, memoryImmediateDelay]
tempFrame.append(tempRow)
tempFrame.extend(immediate + delayed)

for sbj, grp in edatFrame.groupby("Subject"):  
grp is a Frame
groupby([key1, key2])
groupby().groups  is a dict whose keys are the computed unique groups 
                  and corresponding values being the axis labels belonging to each group
                  {'bar': [1, 3, 5], 'foo': [0, 2, 4, 6, 7]}


Loop how to:
for columnName, columnSeries in Frame.iteritems():
    columnIndex = Frame.Columns().index(colName)
    columnUniques = columnSeries.Uniques()
for rowIndex, rowSeries in Frame.iterrows():
for index, value in Series.iteritems():

Also consider apply, applymap, map
apply works on a row / column basis of a DataFrame, applymap works element-wise on a DataFrame, 
and map works element-wise on a Series.    
