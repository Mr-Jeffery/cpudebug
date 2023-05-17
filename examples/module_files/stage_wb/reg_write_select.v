`include "../definitions.v"
`timescale 1ns / 1ps

module reg_write_select (
    input  wb_mem_read_enable,
    input  [`ISA_WIDTH - 1:0] wb_mem_read_data,
    input  [`ISA_WIDTH - 1:0] wb_alu_result,
    output [`ISA_WIDTH - 1:0] wb_result
);

assign wb_result = wb_mem_read_enable ? wb_mem_read_data : wb_alu_result;

endmodule