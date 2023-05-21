
#ifndef CPARSER_H
#define CPARSER_H

#include <verilog_driver.hpp>


class CParser: public verilog::ParserVerilogInterface {
    virtual ~CParser(){}

    void add_module(std::string&& name){
        std::cout << "Module name = " << name << '\n';
    }

    void add_port(verilog::Port&& port) {
        std::cout << "Port: " << port << '\n';
        ports.push_back(std::move(port));
    }

    void add_net(verilog::Net&& net) {
        std::cout << "Net: " << net << '\n';
        nets.push_back(std::move(net));
    }

    void add_assignment(verilog::Assignment&& ast) {
        std::cout << "Assignment: " << ast << '\n';
        assignments.push_back(std::move(ast));
    }

    void add_instance(verilog::Instance&& inst) {
        std::cout << "Instance: " << inst << '\n';
        insts.push_back(std::move(inst));
    }

    void export_signals();

    std::vector<verilog::Port> ports;
    std::vector<verilog::Net> nets;
    std::vector<verilog::Assignment> assignments;
    std::vector<verilog::Instance> insts;
};

#endif // CPARSER_H