import os
import pytest
import zipfile


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
PDF_RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources', 'testpdf.pdf')
TXT_RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources', 'testtxt.txt')
XLS_RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources', 'testxls.xls')
XLSX_RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources', 'testxlsx.xlsx')
TMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'tmp')

@pytest.fixture(scope='session', autouse=True)
def archive_files():
    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH)

        if os.path.exists("archive.zip"):
            os.remove("archive.zip")

    with zipfile.ZipFile(os.path.join(TMP_PATH, 'archive.zip'), mode='a') as zf:
        zf.write(filename=PDF_RESOURCES_PATH, arcname='testpdf.pdf')
        zf.write(filename=TXT_RESOURCES_PATH, arcname='testtxt.txt')
        zf.write(filename=XLS_RESOURCES_PATH, arcname='testxls.xls')
        zf.write(filename=XLSX_RESOURCES_PATH, arcname='testxlsx.xlsx')