import React, { useState, useEffect } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const DysonSphereVisualization = () => {
  const [constructionProgress, setConstructionProgress] = useState(0);
  const [energyOutput, setEnergyOutput] = useState(0);
  const [printerStatus, setPrinterStatus] = useState([]);
  const [temperature, setTemperature] = useState(0);

  useEffect(() => {
    // Simulate construction progress
    const interval = setInterval(() => {
      setConstructionProgress(prev => Math.min(prev + 0.1, 100));
      setEnergyOutput(prev => prev + 1e12);
      setTemperature(5778); // Sun's surface temperature in Kelvin
      setPrinterStatus(Array(5).fill(true));
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <Card className="w-full max-w-4xl mx-auto">
      <CardHeader>
        <CardTitle>Dyson Sphere Construction Progress</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          {/* Progress Indicator */}
          <div className="relative pt-1">
            <div className="flex mb-2 items-center justify-between">
              <div>
                <span className="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full bg-blue-200">
                  Construction Progress
                </span>
              </div>
              <div className="text-right">
                <span className="text-xs font-semibold inline-block">
                  {constructionProgress.toFixed(2)}%
                </span>
              </div>
            </div>
            <div className="overflow-hidden h-2 mb-4 text-xs flex rounded bg-blue-200">
              <div 
                className="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-blue-500"
                style={{ width: `${constructionProgress}%` }}
              />
            </div>
          </div>

          {/* Status Cards */}
          <div className="grid grid-cols-2 gap-4">
            <div className="p-4 bg-gray-100 rounded-lg">
              <h3 className="font-bold mb-2">Energy Output</h3>
              <p>{(energyOutput / 1e12).toFixed(2)} TW</p>
            </div>
            <div className="p-4 bg-gray-100 rounded-lg">
              <h3 className="font-bold mb-2">Surface Temperature</h3>
              <p>{temperature.toFixed(0)}K</p>
            </div>
          </div>

          {/* Printer Status */}
          <div className="p-4 bg-gray-100 rounded-lg">
            <h3 className="font-bold mb-2">3D Printer Status</h3>
            <div className="grid grid-cols-5 gap-2">
              {printerStatus.map((active, index) => (
                <div 
                  key={index}
                  className={`p-2 rounded-full ${active ? 'bg-green-500' : 'bg-red-500'}`}
                >
                  <div className="text-center text-white">
                    #{index + 1}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Construction Metrics */}
          <div className="grid grid-cols-2 gap-4">
            <div className="p-4 bg-gray-100 rounded-lg">
              <h3 className="font-bold mb-2">Material Usage</h3>
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span>Advanced Composite:</span>
                  <span>{(constructionProgress * 1e6).toFixed(0)} tons</span>
                </div>
              </div>
            </div>
            <div className="p-4 bg-gray-100 rounded-lg">
              <h3 className="font-bold mb-2">Completion Estimate</h3>
              <p>{Math.ceil((100 - constructionProgress) / 0.1)} seconds</p>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default DysonSphereVisualization;
