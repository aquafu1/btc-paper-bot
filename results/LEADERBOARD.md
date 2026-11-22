# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1091 windows, 30196 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 570 | 34.6 | 35.0 | $-327.96 | -5.8% | $672.04 | -1.0 | done | can't tell from luck |
| value_ev10 | 1399 | 38.0 | 39.1 | $-888.24 | -6.3% | $111.76 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3052 | 51.0 | 50.5 | $-912.51 | -3.0% | $87.49 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2567 | 49.7 | 49.4 | $-1093.09 | -4.3% | $-93.09 | -2.2 | done | losing for real |
| value_ev5 | 2125 | 40.0 | 41.0 | $-1251.11 | -5.9% | $-251.11 | -2.3 | done | losing for real |
| trend_filter | 1793 | 49.5 | 50.4 | $-1271.80 | -7.1% | $-271.80 | -3.1 | done | losing for real |
| coinflip | 4357 | 50.6 | 50.2 | $-1607.77 | -3.7% | $-607.77 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2567 | 50.3 | 51.1 | $-1674.69 | -6.5% | $-674.69 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3052 | 49.0 | 50.2 | $-1988.06 | -6.5% | $-988.06 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4357 | 50.9 | 51.4 | $-2136.56 | -4.9% | $-1136.56 | -3.3 | done | losing for real |
| always_up | 4357 | 47.5 | 49.3 | $-3537.04 | -8.1% | $-2537.04 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6905 | 48.5 | 49.0 | $-3397.78 |
| ETH | 7480 | 48.2 | 48.4 | $-4388.20 |
| SOL | 7867 | 48.1 | 48.4 | $-4447.48 |
| XRP | 7944 | 48.3 | 48.2 | $-4455.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
