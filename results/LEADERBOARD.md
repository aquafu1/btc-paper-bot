# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 648 windows, 17909 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 337 | 34.7 | 35.3 | $-207.49 | -6.2% | $792.51 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1510 | 50.6 | 49.6 | $-343.57 | -2.3% | $656.43 | -0.9 | done | can't tell from luck |
| value_ev10 | 825 | 38.5 | 39.5 | $-534.77 | -6.5% | $465.23 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1844 | 51.6 | 51.0 | $-544.73 | -3.0% | $455.27 | -1.3 | done | can't tell from luck |
| value_ev5 | 1250 | 41.1 | 41.4 | $-580.13 | -4.6% | $419.87 | -1.4 | done | can't tell from luck |
| trend_filter | 1037 | 49.9 | 50.9 | $-638.76 | -6.2% | $361.24 | -2.0 | done | losing for real |
| coinflip | 2584 | 50.2 | 50.5 | $-1162.94 | -4.5% | $-162.94 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1510 | 49.4 | 51.4 | $-1240.01 | -8.2% | $-240.01 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1844 | 48.4 | 50.0 | $-1266.14 | -6.9% | $-266.14 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2584 | 50.4 | 51.7 | $-1546.63 | -6.0% | $-546.63 | -3.1 | done | losing for real |
| always_up | 2584 | 47.4 | 49.7 | $-2204.15 | -8.5% | $-1204.15 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4062 | 48.3 | 49.3 | $-2451.84 |
| ETH | 4476 | 48.2 | 48.7 | $-2684.85 |
| SOL | 4657 | 48.0 | 48.8 | $-2835.42 |
| XRP | 4714 | 48.5 | 48.6 | $-2297.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
