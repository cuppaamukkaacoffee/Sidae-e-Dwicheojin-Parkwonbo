import React from 'react';


const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'));
const Users = React.lazy(() => import('./views/users/Users'));
const User = React.lazy(() => import('./views/users/User'));
const Webscan = React.lazy(() => import('./views/scan/Webscan'));
const Netscan = React.lazy(() => import('./views/scan/Netscan'));
const Result = React.lazy(() => import('./views/results/Result'));

const routes = [
  { path: '/', exact: true, name: 'Home' },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/users', exact: true,  name: 'Users', component: Users },
  { path: '/users/:id', exact: true, name: 'User Details', component: User },
  { path: '/scan/webscan', exact: true,  name: 'Web scanner', component: Webscan },
  { path: '/scan/netscan', exact: true, name: 'Network scanner', component: Netscan },
  { path: '/result', exact: true, name: 'Results', component: Result },
];

export default routes;
