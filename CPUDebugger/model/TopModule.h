#ifndef TOPMODULE_H
#define TOPMODULE_H
#include "QString"
#include <QList>
#include "Module.h"
/**
 * @brief The TopModule class (deprecated)
 * We have not used yet.
 */
class TopModule {
public:
    void setModule(Module&&);
    void setSignalMap(QString moduleToSignal);
    void flagSignal(QString moduleName, QString signalName);
private:
    QString name;
    QList<Module> subModules;
};

#endif // TOPMODULE_H
