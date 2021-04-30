import React from "react";
import CIcon from "@coreui/icons-react";

const _nav = [
  {
    _tag: "CSidebarNavItem",
    name: "Dashboard",
    to: "/dashboard",
    icon: <CIcon name="cil-speedometer" customClasses="c-sidebar-nav-icon" />,
  },
  {
    _tag: "CSidebarNavTitle",
    _children: ["Scan"],
  },
  {
    _tag: "CSidebarNavDropdown",
    name: "Scanner",
    route: "/scans",
    icon: "cil-speedometer",
    _children: [
      {
        _tag: "CSidebarNavItem",
        name: "Web scan",
        to: "/scans/webscan",
      },
      {
        _tag: "CSidebarNavItem",
        name: "Network scan",
        to: "/scans/netscan",
      },
    ],
  },
  {
    _tag: "CSidebarNavDropdown",
    name: "Target",
    route: "/targets",
    icon: "cil-puzzle",
    _children: [
      {
        _tag: "CSidebarNavItem",
        name: "Web scan",
        to: "/targets/webscan",
      },
      {
        _tag: "CSidebarNavItem",
        name: "Network scan",
        to: "/targets/netscan",
      },
    ],
  },
  {
    _tag: "CSidebarNavItem",
    name: "Vulnerabilities",
    icon: "cil-bell",
    to: "/vulnerabilities",
  },
  {
    _tag: "CSidebarNavDropdown",
    name: "Result",
    route: "/targets",
    icon: "cil-laptop",
    _children: [
      {
        _tag: "CSidebarNavItem",
        name: "Web scan",
        to: "/webresult",
      },
      {
        _tag: "CSidebarNavItem",
        name: "Network scan",
        to: "/netresult",
      },
    ],
  },
  {
    _tag: "CSidebarNavItem",
    name: "User",
    icon: "cil-user",
    to: "/user",
  },
];

export default _nav;
