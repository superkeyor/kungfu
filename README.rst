kungfu
=========
jerryzhujian9 at gmail [\/dot/\] com
Tested under python 2.7
To see your python version
in terminal: python -V
or in python: import sys; print (sys.version)

requires pandas 0.12.0 (tested 0.12.0-2) which will also install numpy etc
download it from https://pypi.python.org/pypi/pandas/0.12.0
or pip install pandas==0.12.0
requires openpyxl version 1.6.1 or higher, but lower than 2.0.0 (tested 1.5.8)
https://pypi.python.org/pypi/openpyxl/1.5.8
pip install openpyxl==1.5.8
=========
"""An enhancement to pandas module.

This is kungfu, with monkey-patched common methods to (Data)Frame and Series in pandas.
Want pandas functions index?  http://pandas.pydata.org/pandas-docs/dev/genindex.html

Usage:
1) import

2) call methods
All the monkey-patched methods use UpperCase names; the original ones use lower_case names.
Generally all of the calling (monkey-patched or not) returns something and the original frame or series remains unchanged.
If user wants the original frame or series to be changed, assign the returns back.

Visualize a series as a column of a frame with the series name being the column name.
Visualize a single list as a series and therefore a column of a frame when converting a series or frame.
However, for a list of lists, Visualize each list of the list (i.e. sublist) as a row!
Memorization: list=series=column

from pandas import isnull as isna
from pandas import isnull as isnull
Frame.read = Frame.Read
Frame.save = Frame.Save
Frame.write = Frame.Save
Frame.pprint = Frame.Print
Frame.play = Frame.Play
Frame.sel = Frame.Sel
Frame.selrow = Frame.SelRow
Frame.delete = Frame.Del
Frame.groupv = Frame.GroupV
Frame.splith = Frame.SplitH
Frame.recols = Frame.ReorderCols
Frame.rerows = Frame.ReorderRows
Frame.rncols = Frame.RenameCols
Frame.newcol = Frame.NewCol
Frame.findval = Frame.FindVal
Frame.countval = Frame.CountVal
Frame.cnames = Frame.Columns
Frame.names = Frame.Columns
Frame.rnames = Frame.Indices
Frame.num = Frame.ToNum
Frame.maskout = Frame.Maskout
# Frame.fillna = Frame.FillNA

Series.play = Series.Play
Series.pprint = Series.Print
Series.sel = Series.Sel
Series.countval = Series.CountVal
# Series.unique = Series.Uniques  --existing method
Series.len = Series.Size
Series.names = Series.Indices
Series.rnames = Series.Indices
Series.cames = Series.Indices
Series.num = Series.ToNum
Series.str = Series.ToStr
Series.maskout = Series.Maskout
# Series.fillna = Series.FillNA

mergelr = MergeLR
concatvh = ConcatVH

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Frame IO, Frame info
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
frame = Frame.Read(path, sep="\t", header=0)
    Read data into a frame. This is a class method.
    Args:
        path, a text or csv file
        sep, character used to separate the file
        header, the row number with header (0=first row, None=no header at all)
    Returns:
        a Frame object with the data.
    Raises:
        None

frame.Print([column=None])
    Print out common useful information of a frame.
    Args:
        optional column name or index; if passed, print out information of only that column instead of that of whole frame.
    Returns:
        None
    Raises:
       None

series.Print()
    Print out useful information of a series.
    Args:
        None
    Returns:
        None
    Raises:
       None

frame.Save(outputFile[, columns=None])
    Save the content of a frame to an excel file or csv file.
    Args:
        the path to the excel file (xlsx), or comma separated (csv); explicitly specify .xlsx or .csv
        optional columns, the order and names of columns to save
            1) can reorder or omit some of the frame's original columns
            2) if skipped, use the frame's original order and names
            3) example: columns=["sbj","Wordpair","UResp","recalled","stage"]
    Returns:
        None
    Raises:
       None

f = Frame.Play()
    Generate a predefine frame for testing, debugging, playing and etc. This is a class method.
    Args:
        None
    Returns:
        a Frame object
    Raises:
       None

s = Series.Play()
    Generate a predefine series for testing, debugging, playing and etc. This is a class method.
    Args:
        None
    Returns:
        a Frame object
    Raises:
       None


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Selection, grouping
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
frame.Sel(*args)
    Select certain columns and rows from a frame.
    Args:
        1) [] for columns FIRST, {} or [] for rows SECOND
        2) if only pass [], treated as columns; if only {}, as rows
        3) additionally, a single int(or str) can be parsed to a list of that int(or str)
        4) int alone or in a list treated as (column/row) index; str alone or in a list as (column/row) name
        5) does NOT support slice; however, one can use the function range(start,stop) to generate a list
        6) better see some examples:
            ('Session') column "Session"
            (1) column 1 (index based, starts from 0)
            (['Session', 1])
                columns "Session" and 1
                the order of selected columns does not have to follow the order in the original frame! could be [2,4,0,1]
            ({'Session': 1}) all columns where "Session" == 1
            ('Session', '0') <---raise error because of '0'
            ('Session', 0) column "Session" and row 0 (index based, starts from 0)
            ('Session', [0, 1]) column "Session" and rows 0 and 1
            ('Session', {'Session': 1}) column "Session" where "Session" == 1
            (0, '0') <---raise error because of '0'
            (0, 0) column 0 and row 0
            (0, [0, 1]) column 0 and rows 0 and 1
            (0, {'Session': 1}) column 0 where "Session" == 1
            (['Session', 1], '0') <---raise error because of '0'
            (['Session', 1], 0) columns "Session" and 1, and row 0
            (['Session', 1], [0, 1]) columns "Session" and 1, and, rows 0 and 1
            (['Session', 1], {"Subject":5101,"Procedure[Trial]":["PresentPair","PresentPair1"]})
                columns "Session" and 1 where "Subject" == 5101 and ("Procedure[Trial]" == "PresentPair" or "Procedure[Trial]" == "PresentPair1")
            ([],0) all columns and row 0
    Returns:
        a Frame object even for a frame with only one column or row
        to select a column or row as a series, use SelCol() or SelRow()
        However, if only a cell is selected, returns the value of that cell with being its own data type.
    Raises:
       None

frame.SelCol(column)
    Select a single column from frame.
    Args:
        a int representing column index or a string representing column name
    Returns:
        a single column as a series
    Raises:
       None

frame.SelRow(row)
    Select a single row from frame.
    Args:
        a int representing row index or a string representing row name
    Returns:
        a single row as a series
    Raises:
       None

frame.Del(*args):
    Delete columns and/or rows from frame.
    Args:
        Same as those for Sel
        if a to-be-deleted column or row does not exist in the frame, it will be ignored
    Returns:
        a Frame object without the passed columns and rows
        when passing an empty columns/rows, this method deletes nothing and returns a Frame object of the same shape
    Raises:
       None

frame.GroupV(edgeMatchSeries, groupColumnName='AutoGroup')
    Edge condition based grouping along the vertical direction

frame.SplitH(subFrameSize=1, resetIndex=True)
    number based splitting along the horizontal direction

series.Sel(elements=[])
    Select elements from a series.
    Args:
        choose one of the three options:
            a int representing index
            a string representing name
            a list of int, a list of str, or a list of int and str
    Returns:
        a list of selected elements. If the list has only one value, return that value instead of a list.
    Raises:
       None



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reorganize
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
General notes on "join":
    when joining along an axis, the index of each frame does not have to in the same order
    e.g. ["a","b","c","f"] for left frame, ["b","c","a","e"] for right frame
    join will match them and return the combined frame (in a certain order)

MergeLR(left, right, join='union', onKeys=[], sort=True)
    Merge 2 frames in the horizontal direction.
    Args:
        left frame, right frame
        join: "left", "right", "union","outer","inter", "inner"
            when a frame column has duplicated values, it will be confusing (i.e. Cartesian product?)
        onKeys:
            1) a list of 2 elements, the first for the left frame, the second for the right
            2) if only one element passed to the list, it is the shared column name in both frames. e.g. ["pair"], or ["@INDEX"]
            3) a list is also considered as one element e.g. onKeys=[["sbj","pair"]]
            4) the element could be a column name in each frame for the join to match
            5) could be the same or different, e.g. ["subject","subject"], or ["name","word"]
            6) a special element name "@INDEX" uses the index of the frame, e.g. ["subject","@INDEX"] or ["@INDEX","@INDEX"]
        sort: whether to sort the final merged frame based on the join-key
    Returns:
        a merged frame
        when merge on a column key rather than an index, in the merged frame, the index will be reset from 0 to n
    Raises:
       None

ConcatVH(frameList, axis=0, join="union", sort=False)
    Concat in the vertical or horizontal direction.
    When concat in the vertical direction, i.e. along index, the horizontal (i.e. along columns) is defined as join direction.
    When concat in the horizontal columns direction, the join direction is the vertical index direction.
    Args:
        frameList should be a list of frame; if want to add a list such as [1,2,3] or a series, convert them first to a frame
        always use a list when considering concat! can concat more than two frames at a time
        axis: the concat direction, 0 or 1
        join:
            1) how the direction other than the concat direction should be handled.
            2) Only handle/match index! (think of it as a specific case of merge method)
            3) possible value: union,outer,inter,inner or a list
                union/outer: match shared ones, preserve unmatched
                inter/inner: mach shared ones, discard unmatched
                or pass a list representing an index, e.g. ["a","b","c"] or frm.Indices().
                With a list passed, it will perform only union with the predefined index; that is, it will ignore join being union or inter.
        sort: True or False
            1) The built-in concat function features:
                When the concating frames have different sequences in the join direction, the join direction is sorted automatically.
                When the concating frames have the same sequence in the join direction, it is not sorted.
                That is, "by default" it will try to sort different, i.e.sort=True.
            2) Hereby, I hacked a bit by providing this sort keyword which does not exist in the built-in concat.
                Set sort=False to disable this feature. So the results are always not sorted, i.e. preserving the original order as much as possible.
                Example: Frame1 is CBDA, Frame2 is CBEDA, concated is then CBDAE (E shows up later in Frame2, but the final order first adopts the order of the Frame1).
            3) See github discussion https://github.com/pydata/pandas/issues/4588
    Returns:
        a Frame object.
    Raises:
       None

frame.ReorderCols(columns=[])
    Reorder columns of a frame.
    Args:
         a list that has equal size to the original columns
    Returns:
        a Frame object
    Raises:
       None

frame.ReorderRows(indices=[])
    Reorder the rows of a frame.
    Args:
        a list that has equal size to the original indices
    Returns:
        a Frame object
    Raises:
       None

frame.RenameCols(newColumns=[])
    Rename the names of each column of a frame.
    Args:
        a list that has equal size to the original columns
        a new column name could be the same as the old one (i.e. not rename)
    Returns:
        a Frame object
    Raises:
       None

frame.NewCol([newColumnName="NewColumn"[, newColumnValue=NA]])
    Append a new column to the frame.
    Args:
        new column name in string
        new column default value
        e.g.frame = frame.NewCol("Wordpair",frame.SelCol("W1") + "-" + frame.SelCol("W2"))
    Returns:
        a Frame object
        this time, the original frame is changed so don't have to assign back to a new frame. but it doesn't hurt
    Raises:
       The new column name should not exist already, otherwise it would overwrite the values of the existing column.



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Stats, Processing
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
IsNA(object)
    Checks whether a string, int, frame, series and etc is np.nan; returns 0 or 1
    Attention, None is a builtin python datatype, IsNA(None) returns true, but series.isin([NA]) will return false

frame.FindVal(valToFind)
    Print out all columns containing valToFind; only allows a single value to be passed each time

frame.CountVal(valToCount)
    Count all occurrence of the valToCount within the frame, can count np.nan, only allows a single value to be passed each time

frame.Columns()
    Returns a list of column names, takes no argument

frame.Indices()
    Returns a list of indices, takes no argument

frame.ToNum()
    Converts possible numbers to num type if they are not, takes no argument
    1) if a column has any number or number-like string, the whole column will be converted to number. Anything that is not a number will be NA
        >>> s=Series(["2323","a"])
        >>> s
        Out[10]:
        0    2323
        1       a
        dtype: object
        >>> s.ToNum()
        Out[11]:
        0    2323
        1     NaN
        dtype: float64
    2) if a column is purely string, it will remain as string.
        >>> t=Series(["adb","s3","sae"])
        >>> t
        Out[13]:
        0    adb
        1     s3
        2    sae
        dtype: object
        >>> t.ToNum()
        Out[14]:
        0    adb
        1     s3
        2    sae
        dtype: object

frame.Maskout(condition)
    1) if a frame cell's value matches the condition, then masked as NA; if not, preserve the original value
    2) returned as a copy; the original frame remains unchanged
    3) condition could be:
        a str, int, list, list of str and int, dict, condition array such as frame > 0
        only one parameter should be passed to the function
        Here are some examples:
            1 --> parsed to frame.isin([1])
            "pad" --> parsed to frame.isin(["pad"])
            [1,"pad"] --> parsed to frame.isin([1,"pad"])
            {"ColumnName":123} --> parsed to frame.isin({"ColumnName":[123]})
            {"ColumnName":["pad","think"]} --> parsed to frame.isin({"ColumnName":["pad","think"]})
            frame > 0 (attendition: if a cell is a string then a string is larger than a number)
        don't pass NA, i.e. Maskout(NA). Why would you do this?

frame.FillNA( *args, **kwargs)
    a re-wrapper of the same frame.fillna()

frame.mean(axis=0),frame.median(axis=0),frame.sum(axis=0)
    axis : index (0), columns (1), by default NA is skipped when calculating, which is nice

frame.corr(method='')
    compute a correlation matrix between all two possible columns; NA excluded
    method could be 'pearson', 'kendall', 'spearman'

series.CountVal(valToCount)
    count all occurrence, can count np.nan as well

series.Uniques()
    returns a list of unique values in a series, takes no argument. Frame does not have a unique method

series.Size()
    returns the number of values in a series (i.e. series length), takes no argument. Frame does not have a size method

series.Indices()
    returns a list of indices of the series, takes no argument

series.ToNum()
    convert possible numbers to num type if they are not
    refer to frame.ToNum()

series.Maskout(condition)
    internally use the Frame.Maskout(); so condition is of the same type

series.FillNA( *args, **kwargs)
    a re-wrapper of the same series.fillna()

series.mean(axis=0),series.median(axis=0),series.sum(axis=0)
    axis : index (0) only, by default NA is skipped which is nice

series.corr(other, method='')
    computer the correlation of a series with another series; NA excluded
    method could be 'pearson', 'kendall', 'spearman'

series = series.ToStr()
    returns the string representation of each element in a series. Frame does not have theses methods.
    then can apply stringmethods, Maskout method to further process
    e.g. series.replace(pattern,replace)
    note: some of these methods are being deprecated
        cat()
        center()
        contains()
        count()
        decode()
        encode()
        endswith()
        extract()
        findall()
        get()
        join()
        len()
        lower()
        lstrip()
        match()
        pad()
        repeat()
        replace()
        rstrip()
        slice()
        slice_replace()
        split()
        startswith()
        strip()
        title()
        upper()

Loop how to:
for columnName, columnSeries in Frame.iteritems():
    columnIndex = Frame.Columns().index(colName)
    columnUniques = columnSeries.Uniques()
for rowIndex, rowSeries in Frame.iterrows():
for index, value in Series.iteritems():