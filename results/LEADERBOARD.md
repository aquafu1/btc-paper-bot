# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 258 windows, 6784 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 675 | 55.6 | 52.2 | $+154.24 | +2.3% | $1154.24 | +0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 544 | 53.3 | 52.1 | $-99.39 | -1.8% | $900.61 | -0.4 | done | can't tell from luck |
| value_ev20 | 119 | 33.6 | 36.7 | $-141.51 | -11.9% | $858.49 | -1.0 | Sun 11:45 AM | too few trades (119/200) |
| value_ev10 | 319 | 36.7 | 40.8 | $-425.19 | -13.3% | $574.81 | -2.0 | done | losing for real |
| trend_filter | 356 | 45.8 | 50.5 | $-485.04 | -13.6% | $514.96 | -2.6 | done | losing for real |
| value_ev5 | 474 | 39.5 | 42.4 | $-526.10 | -11.1% | $473.90 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 544 | 46.7 | 49.8 | $-606.02 | -11.1% | $393.98 | -2.7 | done | losing for real |
| coinflip | 1026 | 49.3 | 50.8 | $-768.85 | -7.5% | $231.15 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1026 | 49.6 | 51.6 | $-831.44 | -8.1% | $168.56 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 675 | 44.4 | 49.8 | $-1004.75 | -14.9% | $-4.75 | -4.0 | done | losing for real |
| always_up | 1026 | 47.3 | 50.2 | $-1061.42 | -10.3% | $-61.42 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1512 | 46.5 | 49.6 | $-1601.63 |
| ETH | 1685 | 46.7 | 49.1 | $-1724.33 |
| SOL | 1762 | 48.1 | 49.3 | $-1439.25 |
| XRP | 1825 | 48.7 | 49.2 | $-1030.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
