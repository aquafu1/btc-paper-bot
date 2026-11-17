# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 636 windows, 17591 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1488 | 51.1 | 49.5 | $-187.87 | -1.3% | $812.13 | -0.5 | done | can't tell from luck |
| value_ev20 | 331 | 33.8 | 35.3 | $-284.70 | -8.6% | $715.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1018 | 50.4 | 50.8 | $-528.48 | -5.2% | $471.52 | -1.7 | done | can't tell from luck |
| value_ev10 | 810 | 38.3 | 39.5 | $-589.42 | -7.3% | $410.58 | -1.7 | done | can't tell from luck |
| value_ev5 | 1227 | 40.6 | 41.4 | $-738.56 | -6.0% | $261.44 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1809 | 51.0 | 51.0 | $-794.53 | -4.4% | $205.47 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1809 | 49.0 | 50.0 | $-1048.91 | -5.8% | $-48.91 | -2.5 | done | losing for real |
| coinflip | 2537 | 50.1 | 50.5 | $-1194.58 | -4.7% | $-194.58 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1488 | 48.9 | 51.4 | $-1417.85 | -9.5% | $-417.85 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2537 | 50.7 | 51.7 | $-1419.10 | -5.6% | $-419.10 | -2.9 | done | losing for real |
| always_up | 2537 | 47.3 | 49.7 | $-2245.20 | -8.8% | $-1245.20 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3993 | 48.3 | 49.3 | $-2427.43 |
| ETH | 4407 | 48.2 | 48.6 | $-2639.97 |
| SOL | 4564 | 48.0 | 48.8 | $-3016.09 |
| XRP | 4627 | 48.5 | 48.5 | $-2365.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
