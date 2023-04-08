#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/2 16:49
# @Author     : yunkong
# @FileName   : main_win.py
# @Description:
import sys
import concurrent.futures

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, \
    QComboBox, QTabWidget, QPlainTextEdit, QCheckBox

import backgound_sacn_func.bk_scan
import finger_ide_func.finger_main
import host_discovery_func.probe_main
import vuln_scan_func.scan_main
import vuln_scan_func.other_vuln_scan


class InputOutputWidget(QWidget):
    def __init__(self, input_label_text, input_widget, output_label_text):
        super().__init__()

        self.input_label = QLabel(input_label_text)
        self.input_widget = input_widget
        self.output_label = QLabel(output_label_text)
        self.output = QTextEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.input_widget)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output)

        self.setLayout(vbox)

    def clear_output(self):
        self.output.clear()


class FingerIdeWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.url_label = QLabel("目标URL：")
        self.url_input = QLineEdit()
        self.output_label = QLabel("扫描结果：")
        self.output_widget = QPlainTextEdit()
        self.start_btn = QPushButton("开始识别")
        self.start_btn.clicked.connect(self.start_scan)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.url_label)
        hbox1.addWidget(self.url_input)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_widget)
        vbox.addWidget(self.start_btn)

        self.setLayout(vbox)

    def start_scan(self):
        # TODO: 实现漏洞扫描功能
        self.output_widget.setPlainText('')
        finger_res = finger_ide_func.finger_main.finger_scan(self.url_input.text())
        for res in list(finger_res):
            self.output_widget.appendPlainText(str(res))
        # self.output_widget.appendPlainText()


class VulnScanWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.protocol_input = QComboBox()
        self.protocol_input.addItems(["http", "https"])
        self.host_label = QLabel("目标HOST：")
        self.host_input = QLineEdit()
        self.service_label = QLabel("目标服务：")
        self.service_input = QComboBox()
        self.service_input.addItems(["weblogic", "log4j", "spring", "django", "drupal", "yongyouOA", "phpmyadmin"])
        self.output_label = QLabel("扫描结果：")
        self.output_widget = QPlainTextEdit()
        self.start_btn = QPushButton("开始扫描")
        self.start_btn.clicked.connect(self.start_scan)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.protocol_input)
        hbox1.addWidget(self.host_label)
        hbox1.addWidget(self.host_input)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.service_label)
        hbox2.addWidget(self.service_input)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_widget)
        vbox.addWidget(self.start_btn)

        self.setLayout(vbox)

    def start_scan(self):
        # TODO: 实现漏洞扫描功能

        self.output_widget.setPlainText('')
        # 创建子线程
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(vuln_scan_func.scan_main.vuln_scan_start, self.protocol_input.currentText(),
                                     self.host_input.text(), self.service_input.currentText())
            for res in future.result():
                self.output_widget.appendPlainText(str(res))


class OtherVulnScanWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.host_label = QLabel("目标HOST：")
        self.host_input = QLineEdit()
        self.port_label = QLabel("目标端口：")
        self.port_input = QLineEdit()
        self.output_label = QLabel("扫描结果：")
        self.output_widget = QPlainTextEdit()
        self.start_btn = QPushButton("开始扫描")
        self.start_btn.clicked.connect(self.start_scan)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.host_label)
        hbox1.addWidget(self.host_input)
        hbox1.addWidget(self.port_label)
        hbox1.addWidget(self.port_input)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_widget)
        vbox.addWidget(self.start_btn)

        self.setLayout(vbox)

    def start_scan(self):
        self.output_widget.setPlainText('')
        # 创建子线程
        res_list = vuln_scan_func.other_vuln_scan.scan_vuln_py(self.host_input.text(), self.port_input.text())
        for res in res_list:
            self.output_widget.appendPlainText(str(res))


class HostDiscoveryWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.net_label = QLabel("目标NAT：")
        self.net_input = QLineEdit()
        self.mask_label = QLabel("子网掩码：")
        self.mask_input = QLineEdit()
        self.output_label = QLabel("扫描结果：")
        self.output_widget = QPlainTextEdit()
        self.start_btn = QPushButton("开始扫描")
        self.start_btn.clicked.connect(self.start_scan)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.net_label)
        hbox1.addWidget(self.net_input)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.mask_label)
        hbox2.addWidget(self.mask_input)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_widget)
        vbox.addWidget(self.start_btn)

        self.setLayout(vbox)

    def start_scan(self):
        # TODO: 实现主机探测功能
        self.output_widget.setPlainText('')
        res_list = host_discovery_func.probe_main.host_probe_start(self.net_input.text(), self.mask_input.text())
        for res in res_list:
            self.output_widget.appendPlainText(str(res))


class BackgroundscanWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.url_label = QLabel("目标URL：")
        self.url_input = QLineEdit()
        self.output_label = QLabel("扫描结果：")
        self.output_widget = QPlainTextEdit()
        self.start_btn = QPushButton("开始扫描")
        self.start_btn.clicked.connect(self.start_scan)

        # 添加多选按钮
        self.php_checkbox = QCheckBox("PHP")
        self.jsp_checkbox = QCheckBox("JSP")
        self.asp_checkbox = QCheckBox("ASP")
        self.dir_checkbox = QCheckBox("DIR")

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.url_label)
        hbox1.addWidget(self.url_input)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.php_checkbox)
        hbox2.addWidget(self.jsp_checkbox)
        hbox2.addWidget(self.asp_checkbox)
        hbox2.addWidget(self.dir_checkbox)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_widget)
        vbox.addWidget(self.start_btn)

        self.setLayout(vbox)

    def start_scan(self):
        # TODO: 实现后台扫描功能
        self.output_widget.setPlainText('')
        dir_list = self.get_checkbox_values()
        res_list = backgound_sacn_func.bk_scan.dir_scan_start(self.url_input.text(), dir_list)
        for res in res_list:
            for key, value in res.items():
                self.output_widget.appendPlainText(key + " : " + value)

    def get_checkbox_values(self):
        scan_options = []
        if self.php_checkbox.isChecked():
            scan_options.append("php")
        if self.jsp_checkbox.isChecked():
            scan_options.append("jsp")
        if self.asp_checkbox.isChecked():
            scan_options.append("asp")
        if self.dir_checkbox.isChecked():
            scan_options.append("dir")
        return scan_options


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.finger_ide_widget = FingerIdeWidget()
        self.vuln_scan_widget = VulnScanWidget()
        self.other_vuln_scan_widget = OtherVulnScanWidget()
        self.host_discovery_widget = HostDiscoveryWidget()
        self.background_scan_Widget = BackgroundscanWidget()
        self.tabs.addTab(self.finger_ide_widget, "指纹识别")
        self.tabs.addTab(self.vuln_scan_widget, "漏洞扫描")
        self.tabs.addTab(self.other_vuln_scan_widget, "其他扫描")
        self.tabs.addTab(self.host_discovery_widget, "主机探测")
        self.tabs.addTab(self.background_scan_Widget, "后台扫描")

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)

        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget {font-size: 20px;}")
    window = MainWindow()
    window.setWindowTitle("Boom box @yunkong")
    window.resize(550, 700)
    window.show()
    sys.exit(app.exec_())
