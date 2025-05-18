import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost', user='boincadm', password='foobar99', db='boincdb')

query = """
SELECT
  r.id                AS result_id,
  r.workunitid        AS workunit_id,
  r.hostid            AS host_id,

  r.create_time       AS result_create_time,
  r.server_state,
  r.outcome,
  r.client_state,
  r.cpu_time,
  r.elapsed_time,
  r.exit_status,
  r.flops_estimate,
  r.peak_working_set_size,
  r.peak_swap_size,
  r.peak_disk_usage,

  w.rsc_fpops_est,
  w.rsc_fpops_bound,
  w.rsc_memory_bound,
  w.rsc_disk_bound,
  w.create_time       AS workunit_create_time,
  w.delay_bound,
  w.error_mask        AS wu_error_mask,
  w.priority,
  w.app_version_num,

  h.p_ncpus,
  h.p_vendor,
  h.p_model,
  h.p_fpops,
  h.p_iops,
  h.p_membw,
  h.os_name,
  h.os_version,
  h.m_nbytes,
  h.m_cache,
  h.m_swap,
  h.d_total,
  h.d_free,
  h.d_boinc_used_total,
  h.d_boinc_used_project,
  h.d_boinc_max,
  h.n_bwup,
  h.n_bwdown,
  h.cpu_efficiency,
  h.duration_correction_factor,
  h.error_rate,
  h.gpu_active_frac,
  h.p_ngpus,
  h.p_gpu_fpops
FROM
  result r
JOIN
  workunit w ON r.workunitid = w.id
JOIN
  host h ON r.hostid = h.id
WHERE
  r.workunitid >= 956
  AND r.workunitid < 1156

"""

df = pd.read_sql(query, conn)
df.to_csv("boinc_result_host_dataset.csv", index=False)

