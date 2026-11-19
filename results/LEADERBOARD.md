# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 800 windows, 22002 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 409 | 33.7 | 34.9 | $-301.28 | -7.4% | $698.72 | -1.1 | done | can't tell from luck |
| value_ev10 | 1007 | 38.0 | 39.1 | $-623.44 | -6.2% | $376.56 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1852 | 50.2 | 49.6 | $-688.05 | -3.7% | $311.95 | -1.6 | done | can't tell from luck |
| trend_filter | 1289 | 50.3 | 50.8 | $-747.79 | -5.8% | $252.21 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2250 | 50.9 | 50.6 | $-826.19 | -3.7% | $173.81 | -1.7 | done | can't tell from luck |
| value_ev5 | 1517 | 40.2 | 41.0 | $-829.17 | -5.5% | $170.83 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 3192 | 51.3 | 51.6 | $-1338.25 | -4.2% | $-338.25 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2250 | 49.1 | 50.2 | $-1340.55 | -6.0% | $-340.55 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1852 | 49.8 | 51.2 | $-1352.02 | -7.3% | $-352.02 | -3.2 | done | losing for real |
| coinflip | 3192 | 50.2 | 50.3 | $-1373.21 | -4.3% | $-373.21 | -2.4 | done | losing for real |
| always_up | 3192 | 47.5 | 49.6 | $-2685.07 | -8.4% | $-1685.07 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4997 | 48.4 | 49.1 | $-2763.81 |
| ETH | 5484 | 48.2 | 48.5 | $-3426.16 |
| SOL | 5734 | 48.3 | 48.6 | $-3123.20 |
| XRP | 5787 | 48.5 | 48.5 | $-2791.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
