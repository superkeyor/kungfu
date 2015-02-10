# The future importation must be in the very first line except comments
from __future__ import division

__author__ = 'jerryzhujian@gmail.com'

__doc__ = """An enhancement to pandas module.
This is kungfu, with monkey-patched common methods to (Data)Frame and Series in pandas.
=============================================
jerryzhujian9_at_gmail.com
Tested under python 2.7
To see your python version
in terminal: python -V
or in python: import sys; print (sys.version)
=============================================
Install:
https://pypi.python.org/pypi/kungfu
pip install kungfu
The above command will auto take care of the following requirements
Requires pandas 0.12.0 (tested 0.12.0-2) which will also install python-dateutil(dateutil), numpy, pytz, six
Requires openpyxl for writing excel (tested with 1.5.8, version 1.6.1 or higher, but lower than 2.0.0 may also work.)
xlrd for reading excel, xlwt for writing .xls (old format) file
(pip install pandas==0.12.0; pip install openpyxl==1.5.8; pip install xlrd; pip install xlwt)


Usage:
Want pandas functions index?
http://pandas.pydata.org/pandas-docs/version/0.12.0/

Call methods
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
Frame.selcol = Frame.SelCol
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
Frame.tolist(), Frame.list()    <--homebrew method
Series.tolist(), Series.list()   <--exisiting method in pandas

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Frame IO, Frame info
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
frame = Frame.Read(path, sep=",", header=0)
    Read data into a frame. This is a class method.
    Args:
        path, a text or csv file
        sep, character used to separate the file, e.g., '\t'
        header, the row number with header (0=first row, None=no header at all)
    Returns:
        a Frame object with the data.
    Raises:
        None
        
frame = Frame.Readx(path, sheetname='Sheet1', header=0)
    Read xlsx, xls file into a frame
    header, the row number with header (0=first row, None=no header at all)

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
"""


#+++++++++++++++++++++++++++++++++++++++++++++++++++++
# import, alias, patch, check etc
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
def CheckPkgVer(pkgName,pkgMinVersion):
    """Makes sure package meet the minimal version."""
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        import pkg_resources
    pkgCurrentVersion = pkg_resources.get_distribution(pkgName).version
    # if pkgCurrentVersion < pkgMinVersion:
    # tested only under version 0.12.0-2
    if pkgCurrentVersion < pkgMinVersion:
        msg = "Error: Requires " + pkgName + " version " + pkgMinVersion + "; The current one is " + pkgCurrentVersion
        raise Exception(msg)

CheckPkgVer("pandas", "0.12.0")


import os, sys, platform, string, random
import numpy
import numpy as np
from numpy import nan as NA
import pandas
import pandas as pd
from pandas import DataFrame
from pandas import DataFrame as Frame
from pandas import Series
from pandas import isnull as IsNA
from pandas import isnull as IsNull


# monkey patch trick from https://mail.python.org/pipermail/python-dev/2008-January/076194.html
def monkeypatch_class(name, bases, namespace):
    assert len(bases) == 1, "Exactly one base class required"
    base = bases[0]
    for name, value in namespace.iteritems():
        if name != "__metaclass__":
            setattr(base, name, value)
    return base


# PatchedFrame and Frame will both have patched methods. But PatchedFrame could not have a docstring at the class level.
class PatchedFrame(Frame):
    __metaclass__ = monkeypatch_class

    @classmethod
    def Read(cls, path, sep=',', header=0, *args, **kwargs):
        """
        (path, sep=',', header=0, *args, **kwargs)
        Read data into a frame. This is a class method.
        Args:
            path, a text or csv file
            sep, character used to separate the file
            header, the row number with header (0=first row, None=no header at all)
        Returns:
            a Frame object with the data
        Raises:
           None
        """
        return pd.read_table(path, sep=sep, header=header, *args, **kwargs)
    
    @classmethod
    def Readx(cls, path, sheetname='Sheet1', header=0, *args, **kwargs):
        """
        (path, sheetname='Sheet1', header=0, *args, **kwargs)
        Read xlsx, xls file into a frame
        Args:
            path, a xlsx, xls file file
            sep, character used to separate the file
            header, the row number with header (0=first row, None=no header at all)
        Returns:
            a Frame object with the data
        Raises:
           None
        """
        return pd.read_excel(path, sheetname=sheetname, header=header, *args, **kwargs)        

    def Save(self, outputFile, columns=None):
        """
        (self, outputFile, columns=None)
        Save the content of a frame to an excel or csv file.
        Args:
            the path to the excel file (xlsx), or csv(.csv, comma separated); explicitly specify .xlsx or .csv 
            optional columns, the order and names of columns to save
                1) can reorder or omit some of the frame's original columns
                2) if skipped, use the frame's original order and names
                3) example: columns=["sbj","Wordpair","UResp","recalled","stage"]
        Returns:
            None
        Raises:
           None
       """
        if outputFile.endswith('.csv'):
            self.to_csv(outputFile, sep=',', na_rep='', float_format="%.3f", cols=columns, header=True, index=False, index_label=None, mode='w', encoding='utf-8')
        else:
            self.to_excel(outputFile, sheet_name='Sheet1', na_rep='', float_format="%.3f", cols=columns, header=True, index=False, index_label=None, startrow=0, startcol=0)

    def Print(self, column=None):
        """
        Print(self, column=None)
        Print out common useful information of a frame.
        Args:
            optional column name or index; if passed, print out information of only that column instead of that of whole frame.
        Returns:
            None
        Raises:
           None
        """
        frameColumns = self.Columns()
        frameIndices = self.Indices()
        frameDtypes = list(self.dtypes)

        if column == None:
            print "This frame has %d columns (%s to %s), %d rows (%s to %s, may not consecutive)" % (len(frameColumns), frameColumns[0], frameColumns[-1], len(frameIndices), frameIndices[0], frameIndices[-1])

            print ""
            print "Column Information:"
            print "Index %28s Name %2s Datatype %-1s #Unique %-1s #Missing %-1s #Total" % ("", "", "", "", "")
            columnIndex = 0
            for columnName, columnSeries in self.iteritems():
                columnUniques = columnSeries.Uniques()
                print "%3d %35s %10s %4d %10d %13d" % (columnIndex, columnName, frameDtypes[columnIndex], len(columnUniques), pd.isnull(columnSeries).sum(), len(frameIndices))
                columnIndex = columnIndex + 1

            print ""
            print "Again, this frame has %d columns (%s to %s), %d rows (%s to %s, may not consecutive)" % (len(frameColumns), frameColumns[0], frameColumns[-1], len(frameIndices), frameIndices[0], frameIndices[-1])

            print ""
            print "Head 5:"
            print self.head()
            print "."
            print "."
            print "."
            print "Tail 5:"
            print self.tail()

        # print only the column
        else:
            if type(column) in [str]:
                columnName = column
                columnIndex = frameColumns.index(columnName)
            elif type(column) in [int,numpy.int32,numpy.int64]:
                columnIndex = column
                columnName = frameColumns[columnIndex]
            columnSeries = self.SelCol(column)
            columnUniques = columnSeries.Uniques()

            print "Column Information:"
            print "Index %28s Name %2s Datatype %-1s #Unique %-1s #Missing %-1s #Total" % ("", "", "", "", "")
            print "%3d %35s %10s %4d %10d %13d" % (columnIndex, columnName, frameDtypes[columnIndex], len(columnUniques), columnSeries.CountVal(NA), len(frameIndices))

            if len(columnUniques) <= 50:
                print ""
                print "Unique values are:"
                print "Index %23s Value %4s Count" % ("", "")
                for index, uniqueValue in enumerate(columnUniques):
                    print "%3d %31s %10d" % (index, uniqueValue, columnSeries.CountVal(uniqueValue))

    @classmethod
    def Play(cls):
        """
        Generate a predefine frame for testing, debugging, playing and etc. This is a class method.
        Args:
            None
        Returns:
            a Frame object
        Raises:
           None
       """
        print "Generating a frame..."
        play = Frame([["hello",3.4,9,np.nan,19821123],["info",-43,0,"ad",'19821123'],["info",0.123,2351,np.nan,'30.102'],["victory",-1.32,101,329]],index=['a','b','c','d'], columns=["AStr","FNum","INum","Mix","Yam"])

        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        play.Print()
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

        print play
        print "Note, one 19821123 and 30.102 are coded as string"
        return play


    def Sel(self, *args):
        """
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
       """
        # normalize all inputs to the form of [],{} or [],[]
        def _PreProcessArgs(args):
            if len(args) == 1:
                cols = args[0]
                if type(cols) in [str,int,numpy.int32,numpy.int64]:
                    return ([cols],{})
                elif type(cols) in [list]:
                    return (cols,{})
                elif type(cols) in [dict]:
                    # a dict should be rows
                    rows = cols
                    for key,value in rows.items():
                        if type(value) not in [list]: rows[key] = [value]
                    return ([],rows)

            elif len(args) == 2:
                cols = args[0]
                rows = args[1]
                # cols
                if type(cols) in [str,int,numpy.int32,numpy.int64]:
                    cols = [cols]
                elif type(cols) in [list]:
                    cols = cols

                # rows
                if type(rows) in [str,int,numpy.int32,numpy.int64]:
                    rows = [rows]
                elif type(rows) in [list]:
                    rows = rows
                elif type(rows) in [dict]:
                    for key,value in rows.items():
                        if type(value) not in [list]: rows[key] = [value]
                return (cols,rows)

        # debug
        # argss = [["Session"],[1],[["Session",1]],[{"Session":1}],["Session","0"],["Session",0],["Session",[0,1]],["Session",{"Session":1}],[0,"0"],[0,0],[0,[0,1]],[0,{"Session":1}],[["Session",1],"0"],[["Session",1],0],[["Session",1],[0,1]],[["Session",1],{"Session":1}]]
        # for args in argss:
        #     print _PreProcessArgs(args)

        def _ProcessArgs(frm,cols,rows):
            # first process cols
            selectedCols = []
            if len(cols) > 0:
                for col in cols:
                    if type(col) in [str]:
                        selectedCols.append(frm.loc[:,col])
                    elif type(col) in [int,numpy.int32,numpy.int64]:
                        selectedCols.append(frm.iloc[:,col])
                selectedCols = pd.concat(selectedCols, join='outer', axis=1)
            else:
                selectedCols = frm

            # now process rows
            if type(rows) in [dict]:
                # all true
                selectedRows = Series(True,index=frm.index)
                for key, value in rows.items():
                    selectedRows = selectedRows & frm[key].isin(value)
                result = selectedCols.loc[selectedRows]
            elif type(rows) in [list]:
                selectedRows = []
                if len(rows) > 0:
                    for row in rows:
                        if type(row) in [str]:
                            selectedRows.append(selectedCols.loc[[row],:])
                        elif type(row) in [int,numpy.int32,numpy.int64]:
                            selectedRows.append(selectedCols.iloc[[row],:])
                else:
                    selectedRows = [selectedCols]
                result = pd.concat(selectedRows, join='outer', axis=0)

            # single element/cell
            return result.iloc[0,0] if result.shape == (1,1) else result

        # debug
        # argss = [(['Session'], {}),([1], {}),(['Session', 1], {}),([], {'Session': [1]}),(['Session'], [0]),(['Session'], [0]),(['Session'], [0, 1]),(['Session'], {'Session': [1]}),([0], [0]),([0], [0]),([0], [0, 1]),([0], {'Session': [1]}),(['Session', 1], [0]),(['Session', 1], [0]),(['Session', 1], [0, 1]),(['Session', 1], {'Session': [1]})]
        # for cols,rows in argss:
        #     print _ProcessArgs(edatFrame,cols,rows)

        if 1<= len(args) <=2:
            (cols,rows) = _PreProcessArgs(args)
            return _ProcessArgs(self,cols,rows)

    def SelCol(self, column):
        """
        (self, column)
        Select a single column from frame.
        Args:
            a int representing column index or a string representing column name
        Returns:
            a single column as a series
        Raises:
           None
        """
        return self.Sel(column).iloc[:,0]

    def SelRow(self, row):
        """
        (self, row)
        Select a single row from frame.
        Args:
            a int representing row index or a string representing row name
        Returns:
            a single row as a series
        Raises:
           None
        """
        return self.Sel([],row).iloc[0,:]

    def Del(self, *args):
        """
        Delete columns and/or rows from frame.
        Args:
            Same as those for Sel
            if a to-be-deleted column or row does not exist in the frame, it will be ignored
        Returns:
            a Frame object without the passed columns and rows
            when passing an empty columns/rows, this method deletes nothing and returns a Frame object of the same shape
        Raises:
           None
        """
        bigFrame = self
        delFrame = bigFrame.Sel(*args)
        diffColumns = [column for column in bigFrame.Columns() if column not in delFrame.Columns()]
        diffIndices = [index for index in bigFrame.Indices() if index not in delFrame.Indices()]
        return bigFrame.Sel(diffColumns,diffIndices)

    def GroupV(self, edgeMatchSeries, groupColumnName='AutoGroup'):
        """
        (self, edgeMatchSeries, groupColumnName='AutoGroup')
        Edge condition based grouping along the vertical direction.
        1) Create a new column and put the group category of each block into this column, such as "G0","G1","G2"
        2) Edge is marked as "Edge"
        3) Later on user can groupby this frame with the new column (default column name is AutoGroup unless user assigns a different one)
        """
        self[groupColumnName] = ''
        groupNum = 0

        for rowIndex, rowSeries in self.iterrows():
                if edgeMatchSeries[rowIndex]:
                    self.ix[rowIndex, groupColumnName] = 'Edge'
                    groupNum += 1
                else:
                    self.ix[rowIndex, groupColumnName] = 'G' + str(groupNum)
        return self

    def SplitH(self, subFrameSize=1, resetIndex=True):
        """
        (self, subFrameSize=1, resetIndex=True)
        Split frame along the horizontal direction into pieces of equal size if possible.
        Args:
            subFrameSize means how many cols each subFrame would have
        """
        # preserve old cols info
        oldColumns = list(self.columns)
        totalColumns = self.columns.size
        # rename cols with numbers starting from 0
        self.columns = xrange(0,totalColumns)

        pieces = []
        for colIndex in xrange(0,totalColumns,subFrameSize):    # xrange takes start,stop,step
            # if exceeds the total number of cols, just append what has left to the last col
            if (colIndex+subFrameSize) > totalColumns:
                pieces.append(self.ix[:,colIndex:])
            else:
                # the range is inclusive; ix bases on names
                pieces.append(self.ix[:,colIndex:(colIndex+subFrameSize-1)])

        # change cols name back to original state
        for p in pieces:
            # the pieces could be unequal size
            p.columns = [oldColumns[0:p.columns.size]]

        if resetIndex:
            # after reset the old index is added as a col called 'index'
            return pd.concat(pieces, join_axes=[oldColumns[0:subFrameSize]]).reset_index().drop('index', axis=1)
        else:
            return pd.concat(pieces, join_axes=[oldColumns[0:subFrameSize]])

    def ReorderCols(self, columns=[]):
        """
        (self, columns=[])
        Reorder columns of a frame.
        Args:
             a list that has equal size to the original columns
        Returns:
            a Frame object
        Raises:
           None
       """
        assert len(columns) == len(self.Columns()), "The total column number should match."
        return self.reindex(columns=columns)

    def ReorderRows(self, indices=[]):
        """
        (self, indices=[])
        Reorder the rows of a frame.
        Args:
            a list that has equal size to the original indices
        Returns:
            a Frame object
        Raises:
           None
        """
        assert len(indices) == len(self.Indices()), "The total indices number should match."
        return self.reindex(index=indices)

    def RenameCols(self, newColumns=[]):
        """
        (self, newColumns=[])
        Rename the names of each column of a frame.
        Args:
            a list that has equal size to the original columns
            a new column name could be the same as the old one (i.e. not rename)
        Returns:
            a Frame object
        Raises:
           None
        """
        assert len(newColumns) == len(self.Columns()), "The total column number should match."
        self.columns = newColumns
        return self

    def NewCol(self, newColumnName="NewColumn", newColumnValue=NA):
        """
        (self, newColumnName="NewColumn", newColumnValue=NA)
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
        """
        assert newColumnName not in self.Columns(), "The new column name should not be the same as the existing one."
        self[newColumnName] = newColumnValue
        return self

    def FindVal(self, valToFind, *args):
        """
        (self, valToFind, *args)
        Print out all columns containing valToFind; only allows a single value to be passed each time
        """
        assert len(args) == 0, "Only one value should be passed at a time."
        for colName, colSeries in self.iteritems():
            if valToFind in colSeries.unique():
                print "+++++++++++++++++++++++++++++++++++++++++"
                print "column " + colName + " has " + str(valToFind)
                self.Print(colName)
                print "+++++++++++++++++++++++++++++++++++++++++"

    def CountVal(self, valToCount, *args):
        """
        (self, valToCount, *args)
        Count all occurrence of the valToCount within the frame, can count np.nan, only allows a single value to be passed each time
        """
        assert len(args) == 0, "Only one value should be passed at a time."
        # np.where reports error if valToCount is a string
        # return np.where(self == valToCount, 1, 0).sum()
        # np.nan does not work for value == valToCount because np.nan is designed not equal to itself
        # pd.isnull is the omnibus
        if pd.isnull(valToCount):
            return pd.isnull(self).sum().sum(axis=1)
        else:
            sum = 0
            for colName, colSeries in self.iteritems():
                for index, value in colSeries.iteritems():
                    if value == valToCount:
                        sum += 1
            return sum

    def Columns(self):
        """Returns a list of column names, takes no argument"""
        if len(self.columns) == 0:
            result = []
        else:
            # when column does not have a name, it uses a numpy.int64 as its name. Then convert to python int.
            if type(self.columns[0]) in [numpy.int32,numpy.int64]:
                result = [int(column) for column in self.columns]
            else:
                result = list(self.columns)
        return result

    def Indices(self):
        """Returns a list of indices, takes no argument"""
        if len(self.index) == 0:
            result = []
        else:
            if type(self.index[0]) in [numpy.int32,numpy.int64]:
                result = [int(i) for i in self.index]
            else:
                result = list(self.index)
        return result

    def ToNum(self):
        """
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
        """
        return self.convert_objects(convert_dates=True, convert_numeric=True, copy=True)

    def ToList(self):
        """returns a list representation of a frame"""
        return self.values.tolist()
        
    def Maskout(self, condition):
        """
        (self, condition)
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
        """
        # this isin is largely copied (with few modifications) from version 0.13 of pandas
        # because currently I am working on version 0.12; version 0.13 introduces Frame.isin()
        def _FrameIsIn(frm, values):
            """
            Return boolean DataFrame showing whether each element in the
            DataFrame is contained in values.

            Parameters
            ----------
            values : iterable, Series, DataFrame or dictionary
                The result will only be true at a location if all the
                labels match. If `values` is a Series, that's the index. If
                `values` is a dictionary, the keys must be the column names,
                which must match. If `values` is a DataFrame,
                then both the index and column labels must match.

            Returns
            -------

            DataFrame of booleans

            Examples
            --------
            When ``values`` is a list:

            >>> df = DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'f']})
            >>> df.isin([1, 3, 12, 'a'])
                   A      B
            0   True   True
            1  False  False
            2   True  False

            When ``values`` is a dict:

            >>> df = DataFrame({'A': [1, 2, 3], 'B': [1, 4, 7]})
            >>> df.isin({'A': [1, 3], 'B': [4, 7, 12]})
                   A      B
            0   True  False  # Note that B didn't match the 1 here.
            1  False   True
            2   True   True

            When ``values`` is a Series or DataFrame:

            >>> df = DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'f']})
            >>> other = DataFrame({'A': [1, 3, 3, 2], 'B': ['e', 'f', 'f', 'e']})
            >>> df.isin(other)
                   A      B
            0   True  False
            1  False  False  # Column A in `other` has a 3, but not at index 1.
            2   True   True
            """
            # modification begins
            # convert a single str or int to a list
            if type(values) in [str,int,numpy.int32,numpy.int64]: values = [values]
            # modification ends
            if isinstance(values, dict):
                from collections import defaultdict
                from pandas.tools.merge import concat
                values = defaultdict(list, values)
                # modification begins
                # this is recursive calling, the original statement is
                # return concat((self.iloc[:, [i]].isin(values[col])
                #                for i, col in enumerate(self.columns)), axis=1)
                return concat((_FrameIsIn(frm.iloc[:, [i]],values[col])
                               for i, col in enumerate(frm.columns)), axis=1)
                # modification ends
            elif isinstance(values, Series):
                if not values.index.is_unique:
                    raise ValueError("ValueError: cannot compute isin with"
                                     " a duplicate axis.")
                return frm.eq(values.reindex_like(frm), axis='index')
            elif isinstance(values, DataFrame):
                if not (values.columns.is_unique and values.index.is_unique):
                    raise ValueError("ValueError: cannot compute isin with"
                                     " a duplicate axis.")
                return frm.eq(values.reindex_like(frm))
            else:
                import pandas.lib as lib
                from pandas.core.common import is_list_like
                if not is_list_like(values):
                    raise TypeError("only list-like or dict-like objects are"
                                    " allowed to be passed to DataFrame.isin(), "
                                    "you passed a "
                                    "{0!r}".format(type(values).__name__))
                return DataFrame(lib.ismember(frm.values.ravel(),
                                              set(values)).reshape(frm.shape),
                                 frm.index,
                                 frm.columns)

        # preprocess
        if type(condition) in [int,numpy.int32,numpy.int64,str]:
            condition = [condition]
        # if a list (including list converted from the int and str above) or a dict
        # pass directly to the _FrameIsIn() which will return a frame of the same shape with values of True/False
        if type(condition) in [list,dict]:
            cndArray = _FrameIsIn(self,condition)
        # although _FrameIsIn() can accept a Frame or Series, leave this kind of types for situation like this:
        # Frame > 0 also generates a Frame (which has values of True/False)
        # if a Series is passed, convert to a Frame first
        if isinstance(condition, Series):
            condition = Frame(condition)
        if isinstance(condition, DataFrame):
            cndArray = condition

        # process
        # basically the mask does this:
        # if a Frame cell's value is True in the cndArray, then masked as NA in the original frame
        # if not, preserve the original value
        return self.mask(cndArray)

    def FillNA(self,  *args, **kwargs):
        """a re-wrapper of the same frame.fillna()"""
        return self.fillna( *args, **kwargs)



# PatchedSeries and Series will both have patched methods. But PatchedSeries could not have a docstring at the class level.
class PatchedSeries(Series):
    __metaclass__ = monkeypatch_class

    @classmethod
    def Play(cls):
        """
        Generate a predefine series for testing, debugging, playing and etc. This is a class method.
        Args:
            None
        Returns:
            a Series object
        Raises:
           None
        """
        print "Generating a series..."
        play = Series(["8.12","x*0_9i",np.nan,-9.3890,2],index=['a','b','c','d','e'],name="Ser")

        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        play.Print()
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

        print play
        print "Note, 8.12 is coded as string."
        return play


    def Print(self):
        """
        (self)
        Print out useful information of a series.
        Args:
            None
        Returns:
            None
        Raises:
           None
        """
        ser = self
        serName = ser.name
        serDatatype = str(ser.dtype)
        serUniques = ser.Uniques()
        serMissingNum = ser.CountVal(NA)
        serIndices = ser.Indices()
        serTotalNum = len(serIndices)

        print "This series has %d values (%s to %s, may not consecutive)" % (serTotalNum, serIndices[0], serIndices[-1])

        print ""
        print "Name: %s, Datatype: %s, #Unique: %d, #Missing: %d, #Total %d" % (serName, serDatatype, len(serUniques), serMissingNum, serTotalNum)

        print ""
        print ser

        if len(serUniques) <= 50:
            print ""
            print "Unique values are:"
            print "Index %23s Value %4s Count" % ("", "")
            for index, uniqVal in enumerate(serUniques):
                print "%3d %31s %10d" %(index, uniqVal, ser.CountVal(uniqVal))

    def Sel(self, elements=[]):
        """
        (self, elements=[])
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
        """
        # preprocess
        if type(elements) in [str,int,numpy.int32,numpy.int64]:
            elements = [elements]

        # process
        selected = []
        for i in elements:
            if type(i) in [str]:
                selected.append(self.loc[i])
            elif type(i) in [int,numpy.int32,numpy.int64]:
                selected.append(self.iloc[i])

        # if only one selected, do not return a list
        return selected[0] if len(selected) == 1 else selected

    def CountVal(self, valToCount):
        """
        (self, valToCount)
        count all occurrence, can count np.nan as well
        """
        if pd.isnull(valToCount):
            return self.isnull().sum()
        else:
            sum = 0
            for index, value in self.iteritems():
                if value == valToCount:
                    sum += 1
            return sum

    def Uniques(self):
        """returns a list of unique values in a series, takes no argument. Frame does not have a unique method"""
        return list(self.unique())

    def Size(self):
        """returns the number of values in a series (i.e. series length), takes no argument. Frame does not have a size method"""
        return self.size        

    def Indices(self):
        """returns a list of indices of the series, takes no argument"""
        if len(self.index) == 0:
            result = []
        else:
            if type(self.index[0]) in [numpy.int32,numpy.int64]:
                result = [int(i) for i in self.index]
            else:
                result = list(self.index)
        return result

    def ToNum(self):
        """convert possible numbers to num type if they are not, refer to frame.ToNum()"""
        return self.convert_objects(convert_dates=True, convert_numeric=True, copy=True)

    def ToStr(self):
        """
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
        """
        return self.str

    def Maskout(self, condition):
        """
        (self, condition)
        internally use the Frame.Maskout(); so condition is of the same type
        """
        theSeries = self
        theSeriesFrame = Frame(theSeries)
        theSeriesFrameMasked = theSeriesFrame.Maskout(condition)
        theSeries = theSeriesFrameMasked.SelCol(0)
        return theSeries

    def FillNA(self, *args, **kwargs):
        """a re-wrapper of the same series.fillna()"""
        return self.fillna( *args, **kwargs)




def MergeLR(left, right, join='union', onKeys=[], sort=True):
    """
    (left, right, join='union', onKeys=[], sort=True)
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
    """
    # default values for the default merge function
    on = None
    left_on = None
    right_on = None
    left_index = False
    right_index = False
    # remap
    if join == "union":
        join = "outer"
    elif join == "inter":
        join = "inner"
    # onkeys should be a list
    # if only one element, then it is the shared key
    if len(onKeys) == 1:
        if onKeys[0] == "@INDEX":
            left_index = True
            right_index = True
        else:
            on = onKeys[0]
    elif len(onKeys) == 2:
        leftKey = onKeys[0]
        rightKey = onKeys[1]
        if leftKey == "@INDEX":
            left_index = True
        else:
            left_on = leftKey
        if rightKey == "@INDEX":
            right_index = True
        else:
            right_on = rightKey
    return pd.merge(left, right, how=join, on=on, left_on=left_on, right_on=right_on, left_index=left_index, right_index=right_index, sort=sort, suffixes=('_x', '_y'), copy=True)


def ConcatVH(frameList, axis=0, join="union", sort=False):
    """
    (frameList, axis=0, join="union", sort=False)
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
    """
    # default value for the default concat function
    join_axes = None
    # axis defines the direction along which to concat
    # join defines the way of index matching (match only index!) in the other direction other than the concat direction
    # union/outer: match the shared ones, preserve unmatched, no information lost
    # the default function uses outer/inner. Here I remap from union/inter
    if join == "union":
        join = "outer"
    # inter/inner: only common/shared information is saved, discard unmatched
    elif join == "inter":
        join = "inner"
    # ignore the matching of either union or inter, simply use a predefined index
    # even though you set join="inner", if you still have a unmatched index in the join_axes, you WILL get the unmatched index in the result
    # even if you define an unexisting index, you WILL have it too.
    # the bottom line is (seems to be): join_axes ignores join value, and then do the Union with what is in the join_axes
    # also, the value should be a list of list, because it is for ALL join axES. e.g. [edatFrame.index],[["a","b","c"]]
    # here I hacked, so only a normal list SHOULD be passed
    elif type(join) in [list]:
        join_axes = [join]
        join = "outer"
    # in case still use "outer, inner" instead of "union, inter"
    else:
        join = join
    # there are other parameters for pd.concat, I don't wanna play with it now... These are common and maybe enough.
    # potentially sorted
    sorted = pd.concat(frameList, axis=axis, join=join, join_axes=join_axes, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False)

    if join_axes:
        return sorted
    elif sort:
        return sorted
    else:
        # expand all original orders in each frame
        sourceOrder = []
        for frame in frameList:
            sourceOrder.extend(frame.Columns()) if axis == 0 else sourceOrder.extend(frame.Indices())
        sortedOrder = sorted.Columns() if axis == 0 else sorted.Indices()

        positions = []
        positionsSorted = []
        for i in sortedOrder:
            positions.append(sourceOrder.index(i))
            positionsSorted.append(sourceOrder.index(i))
        positionsSorted.sort()

        unsortedOrder = []
        for i in positionsSorted:
            unsortedOrder.append(sortedOrder[positions.index(i)])

        return sorted.ReorderCols(unsortedOrder) if axis == 0 else sorted.ReorderRows(unsortedOrder)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# refractory to lower cases
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from pandas import isnull as isna
from pandas import isnull as isnull
Frame.read = Frame.Read
Frame.readx = Frame.Readx
Frame.save = Frame.Save
Frame.write = Frame.Save
Frame.pprint = Frame.Print
Frame.play = Frame.Play
Frame.sel = Frame.Sel
Frame.selcol = Frame.SelCol
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
Frame.tolist = Frame.ToList
Frame.list = Frame.ToList
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
Series.ToList = Series.tolist
Series.list = Series.tolist
# Series.fillna = Series.FillNA

mergelr = MergeLR
concatvh = ConcatVH


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# debugging
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":

    df4a = DataFrame(columns=['C','B','D','A'], data=np.random.randn(3,4))
    df4b = DataFrame(columns=['C','B','D','A'], data=np.random.randn(3,4))
    df5  = DataFrame(columns=['C','B','E','D','A'], data=np.random.randn(3,5))

    ConcatVH([df4a,df5])

    print "Cols unsorted:", pd.concat([df4a,df4b])
    # Cols unsorted:           C         B         D         A

    print "Cols sorted", pd.concat([df4a,df5])



    ## only for debugging, playing

    f = Frame.Play()
    s = Series.Play()

    f1 = f.Sel([0,1])
    f2 = f.Sel([1,2])

    IsNA(f)
    print NA

    f1.Print()
    f2.Print("FNum")
    f2.Print(1)

    s.Print()

    f.Save("output.xlsx",["AStr"])
    f.Save("output1.xlsx")
    f.Save("output2.xlsx",["FNum","AStr","Mix","Yam"])

    c = ConcatVH([f1,f2],axis=0,join="union") ;print c
    c = ConcatVH([f1,f2],axis=1,join="union")   ;print c
    c = ConcatVH([f1.ReorderCols(["FNum","AStr"]),f2.ReorderRows(["b","a","c","d"])],axis=1,join="outer");print c
    c = ConcatVH([f1,f2],axis=1,join="inner")     ;print c
    c = ConcatVH([f1,f2],axis=1,join="inter")       ;print c
    c = ConcatVH([f1,f2],axis=1,join=["a","b","C"])   ;print c

    f3 = f1.ReorderCols(["FNum","AStr"]);print f3
    f4 = f2.ReorderRows(["b","a","c","d"]);print f4
    m = MergeLR(f3,f4,join="union", onKeys=["FNum","FNum"]);print m
    m = MergeLR(f3,f4,join="inner", onKeys=["FNum"]);print m
    m = MergeLR(f3,f4,join="inner", onKeys=["@INDEX"]);print m
    m = MergeLR(f3,f4,join="outer", onKeys=["@INDEX"]);print m
    m = MergeLR(f3,f4,join="inter", onKeys=["@INDEX"]);print m

    m = MergeLR(f1,f2,join="inner", onKeys=["FNum"]);print m



    h = f1.Sel(0); print h
    h = f1.Sel("AStr"); print h
    h = f1.Sel(["AStr"],0); print h
    h = f1.Sel(["AStr"],"b"); print h
    h = f1.Sel({"FNum":0.123}); print h

    h = f.Sel({"Yam":None}); print h


    h = f1.SelCol(0); print h
    h = f1.SelCol("AStr"); print h

    h = f1.SelRow(0); print h
    h = f1.SelRow("a"); print h

    # argss = [(['AStr'], {}),([1], {}),(['AStr', 1], {}),([], {'AStr': [1]}),(['AStr'], ['0']),(['AStr'], [0]),(['AStr'], [0, 1]),(['AStr'], {'AStr': [1]}),([0], ['0']),([0], [0]),([0], [0, 1]),([0], {'AStr': [1]}),(['AStr', 1], ['0']),(['AStr', 1], [0]),(['AStr', 1], [0, 1]),(['AStr', 1], {'AStr': [1]})]
    # replace '0'
    argss = [(['AStr'], {}),([1], {}),(['AStr', 1], {}),([], {'AStr': [1]}),(['AStr'], [0]),(['AStr'], [0]),(['AStr'], [0, 1]),(['AStr'], {'AStr': [1]}),([0], [0]),([0], [0]),([0], [0, 1]),([0], {'AStr': [1]}),(['AStr', 1], [0]),(['AStr', 1], [0]),(['AStr', 1], [0, 1]),(['AStr', 1], {'AStr': [1]})]
    for cols,rows in argss:
         print f.Sel(cols,rows)

    h = f1.Sel("AStr").RenameCols(["Astr"])
    h.NewCol("new")
    h.NewCol()
    h.NewCol("newc","log")
    print h

    f.FindVal(NA)
    f.FindVal(19821123)

    print f.CountVal(NA)
    print f.CountVal(19821123)

    print f.Columns()
    print f.Indices()

    f.ToNum().Print()

    print f.Maskout(0)
    #print f.Maskout(NA)
    print f.Maskout([0,NA])
    print f.Maskout({"Yam":19821123})
    print f.Maskout(f>0)

    print f.FillNA(999999)

    #######################################
    print s.Sel(0)
    print s.Sel([0,1])
    print s.Sel([0,"d"])
    print s.Sel("d")
    print
    print s.CountVal(NA)
    print s.Uniques()
    print s.Indices()
    print
    print s.ToNum()
    print
    t = s.ToStr()
    print t.contains("_")
    print s.Maskout("x*0_9i")
    print s.Maskout(2)
    print s.Maskout(s>0)
    print
    print s.FillNA(9999999)