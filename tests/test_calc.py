import pytest
import os
import pathlib
import xarray as xr
from cesm_collections import calc

sample_data_dir = pathlib.Path(os.path.dirname(__file__)).parent / 'data'

@pytest.mark.parametrize(
    'data',
    [sample_data_dir / 'silver_linings' / 'b.e21.BW.f09_g17.SSP245-TSMLT-GAUSS-LOWER-0.5.001.cam.h0.2035-01.nc',
     sample_data_dir / 'mom_pop' / 'pop' / 'pop_no_mcog.pop.h.0001-01.nc' 
    ],
)
def test_center_time(data):
    ds = xr.open_dataset(data)
    ds_center_time = calc.center_time(ds)
    assert isinstance(ds_center_time, xr.Dataset)