# Copyright 2020 Ford Motor Company 

 

# Licensed under the Apache License, Version 2.0 (the "License"); 

# you may not use this file except in compliance with the License. 

# You may obtain a copy of the License at 

 

#     http://www.apache.org/licenses/LICENSE-2.0 

 

# Unless required by applicable law or agreed to in writing, software 

# distributed under the License is distributed on an "AS IS" BASIS, 

# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 

# See the License for the specific language governing permissions and 

# limitations under the License. 

from cookiecutterassert.rules.rules_util import readLinesFromFile

expectedLines = [
    "line0",
    "line1",
    "looking for this line",
    "line2"
]

def test_readLinesFromFile_shouldReadLinesFromFile():
    assert readLinesFromFile("fileWithLine.txt", folder="example") == expectedLines

def test_readLinesFromFile_shouldReadLinesFromFQPath():
    assert readLinesFromFile("example/fileWithLine.txt") == expectedLines

def test_readLinesFromFile_shouedPreserveNewlinesIfAsked():
    expectedLinesWithNewlines = []
    for line in expectedLines:
        expectedLinesWithNewlines.append(line+"\n")
    expectedLinesWithNewlines[-1] = expectedLines[-1]
    assert readLinesFromFile("fileWithLine.txt", folder="example", removeNewline=False) == expectedLinesWithNewlines
