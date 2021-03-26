import React from 'react';


const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'));
const User = React.lazy(() => import('./views/users/User'));
const Webscan = React.lazy(() => import('./views/scan/Webscan'));
const Netscan = React.lazy(() => import('./views/scan/Netscan'));
const Result = React.lazy(() => import('./views/results/Result'));
const Web_targets = React.lazy(() => import('./views/results/Web_targets'));
const Net_targets = React.lazy(() => import('./views/results/Net_targets'));
const Vulnerabilities = React.lazy(() => import('./views/results/Vulnerabilities'));
const Report = React.lazy(() => import('./views/results/Report'));
const Detail = React.lazy(() => import('./views/results/Detail'));
const Net_detail = React.lazy(() => import('./views/results/Net_detail'));

const routes = [
  { path: '/', exact: true, name: 'Home' },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/user', exact: true, name: 'User profile', component: User },
  { path: '/scans/webscan', exact: true,  name: 'Web scanner', component: Webscan },
  { path: '/scans/netscan', exact: true, name: 'Network scanner', component: Netscan },
  { path: '/result', exact: true, name: 'Results', component: Result },
  { path: '/targets/webscan', exact: true, name: 'Web Scan Target', component: Web_targets },
  { path: '/targets/netscan', exact: true, name: 'Network Scan Target', component: Net_targets },
  { path: '/vulnerabilities', exact: true, name: 'Vulnerabilities', component: Vulnerabilities },
  { path: '/report', exact: true, name: 'Report', component: Report },
  { path: '/detail', exact: true, name: 'Detail', component: Detail },
  { path: '/netdetail', exact: true, name: 'Net Detail', component: Net_detail },
];

export default routes;
