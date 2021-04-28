import React from "react";

const Dashboard = React.lazy(() => import("./views/dashboard/Dashboard"));
const User = React.lazy(() => import("./views/users/User"));
const Webscan = React.lazy(() => import("./views/scan/Webscan"));
const Netscan = React.lazy(() => import("./views/scan/Netscan"));
const Web_result = React.lazy(() => import("./views/results/Web_result"));
const Net_result = React.lazy(() => import("./views/results/Net_result"));
const Web_targets = React.lazy(() => import("./views/results/Web_targets"));
const Net_targets = React.lazy(() => import("./views/results/Net_targets"));
const Vulnerabilities = React.lazy(() =>
  import("./views/results/Vulnerabilities")
);
const Report = React.lazy(() => import("./views/results/Report"));
const Web_detail = React.lazy(() => import("./views/results/Web_detail"));
const Net_detail = React.lazy(() => import("./views/results/Net_detail"));

const routes = [
  { path: "/", exact: true, name: "Home" },
  { path: "/dashboard", name: "Dashboard", component: Dashboard },
  { path: "/user", exact: true, name: "User Profile", component: User },
  {
    path: "/scans/webscan",
    exact: true,
    name: "Web Scanner",
    component: Webscan,
  },
  {
    path: "/scans/netscan",
    exact: true,
    name: "Network Scanner",
    component: Netscan,
  },
  {
    path: "/webresult",
    exact: true,
    name: "Web Scan Results",
    component: Web_result,
  },
  {
    path: "/netresult",
    exact: true,
    name: "Network Scan Results",
    component: Net_result,
  },
  {
    path: "/targets/webscan",
    exact: true,
    name: "Web Scan Target",
    component: Web_targets,
  },
  {
    path: "/targets/netscan",
    exact: true,
    name: "Network Scan Target",
    component: Net_targets,
  },
  {
    path: "/vulnerabilities",
    exact: true,
    name: "Vulnerabilities",
    component: Vulnerabilities,
  },
  { path: "/report", exact: true, name: "Report", component: Report },
  {
    path: "/webdetail",
    exact: true,
    name: "Web Scan Detail",
    component: Web_detail,
  },
  {
    path: "/netdetail",
    exact: true,
    name: "Network Scan Detail",
    component: Net_detail,
  },
];

export default routes;
