# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 587 windows, 16272 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1385 | 51.2 | 49.6 | $-216.76 | -1.6% | $783.24 | -0.6 | done | can't tell from luck |
| value_ev20 | 319 | 33.5 | 35.2 | $-317.78 | -10.0% | $682.22 | -1.4 | done | can't tell from luck |
| trend_filter | 946 | 50.3 | 50.9 | $-524.37 | -5.5% | $475.63 | -1.7 | done | can't tell from luck |
| value_ev10 | 764 | 37.7 | 39.4 | $-666.56 | -8.7% | $333.44 | -2.0 | done | losing for real |
| value_ev5 | 1142 | 40.3 | 41.3 | $-763.31 | -6.7% | $236.69 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1651 | 50.8 | 51.0 | $-811.63 | -4.9% | $188.37 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1651 | 49.2 | 49.9 | $-939.16 | -5.7% | $60.84 | -2.3 | done | losing for real |
| coinflip | 2343 | 49.9 | 50.5 | $-1224.54 | -5.2% | $-224.54 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1385 | 48.8 | 51.3 | $-1345.19 | -9.7% | $-345.19 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2343 | 50.1 | 51.8 | $-1667.39 | -7.1% | $-667.39 | -3.6 | done | losing for real |
| always_up | 2343 | 47.3 | 49.8 | $-2171.00 | -9.3% | $-1171.00 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3690 | 47.8 | 49.2 | $-2708.52 |
| ETH | 4062 | 48.0 | 48.6 | $-2622.21 |
| SOL | 4229 | 47.9 | 48.8 | $-3027.81 |
| XRP | 4291 | 48.5 | 48.6 | $-2289.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
