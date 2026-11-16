# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 554 windows, 15373 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1308 | 51.3 | 49.7 | $-238.15 | -1.8% | $761.85 | -0.7 | done | can't tell from luck |
| value_ev20 | 303 | 33.3 | 35.2 | $-325.92 | -10.8% | $674.08 | -1.4 | done | can't tell from luck |
| trend_filter | 891 | 50.5 | 51.0 | $-489.63 | -5.5% | $510.37 | -1.7 | done | can't tell from luck |
| value_ev10 | 728 | 37.2 | 39.3 | $-722.65 | -9.9% | $277.35 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1561 | 49.3 | 49.8 | $-837.96 | -5.4% | $162.04 | -2.1 | done | losing for real |
| value_ev5 | 1083 | 39.7 | 41.2 | $-857.77 | -7.9% | $142.23 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1561 | 50.7 | 51.1 | $-898.22 | -5.8% | $101.78 | -2.3 | done | losing for real |
| coinflip | 2210 | 50.0 | 50.5 | $-1232.03 | -5.6% | $-232.03 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1308 | 48.7 | 51.2 | $-1301.20 | -9.9% | $-301.20 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2210 | 50.3 | 51.8 | $-1546.46 | -7.0% | $-546.46 | -3.4 | done | losing for real |
| always_up | 2210 | 46.8 | 49.9 | $-2363.66 | -10.7% | $-1363.66 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3477 | 47.5 | 49.2 | $-2776.67 |
| ETH | 3827 | 47.9 | 48.6 | $-2711.61 |
| SOL | 4007 | 47.8 | 48.7 | $-3004.59 |
| XRP | 4062 | 48.5 | 48.6 | $-2320.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
