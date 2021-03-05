import React from 'react';


const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'));
const User = React.lazy(() => import('./views/users/User'));
const Webscan = React.lazy(() => import('./views/scan/Webscan'));
const Netscan = React.lazy(() => import('./views/scan/Netscan'));
const Result = React.lazy(() => import('./views/results/Result'));
const Target = React.lazy(() => import('./views/results/Target'));
const Vulnerabilities = React.lazy(() => import('./views/results/Vulnerabilities'));
const Report = React.lazy(() => import('./views/results/Report'));

const routes = [
  { path: '/', exact: true, name: 'Home' },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/user', exact: true, name: 'User profile', component: User },
  { path: '/scans/webscan', exact: true,  name: 'Web scanner', component: Webscan },
  { path: '/scans/netscan', exact: true, name: 'Network scanner', component: Netscan },
  { path: '/result', exact: true, name: 'Results', component: Result },
  { path: '/target', exact: true, name: 'Target', component: Target },
  { path: '/vulnerabilities', exact: true, name: 'Vulnerabilities', component: Vulnerabilities },
  { path: '/report', exact: true, name: 'Report', component: Report },
];

export default routes;
