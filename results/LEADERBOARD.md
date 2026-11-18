# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 5:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 756 windows, 20852 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 394 | 33.8 | 34.9 | $-291.45 | -7.4% | $708.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2128 | 51.5 | 50.6 | $-488.76 | -2.3% | $511.24 | -1.1 | done | can't tell from luck |
| value_ev10 | 957 | 38.0 | 39.1 | $-597.58 | -6.2% | $402.42 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1763 | 50.0 | 49.6 | $-668.66 | -3.8% | $331.34 | -1.6 | done | can't tell from luck |
| value_ev5 | 1441 | 40.4 | 41.1 | $-766.64 | -5.3% | $233.36 | -1.7 | done | can't tell from luck |
| trend_filter | 1227 | 49.9 | 50.9 | $-795.35 | -6.5% | $204.65 | -2.3 | done | losing for real |
| coinflip | 3017 | 50.4 | 50.3 | $-1109.94 | -3.7% | $-109.94 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1763 | 50.0 | 51.2 | $-1202.60 | -6.8% | $-202.60 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2128 | 48.5 | 50.2 | $-1547.98 | -7.3% | $-547.98 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3017 | 50.9 | 51.8 | $-1609.06 | -5.3% | $-609.06 | -3.0 | done | losing for real |
| always_up | 3017 | 46.9 | 49.6 | $-2900.40 | -9.6% | $-1900.40 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4725 | 48.1 | 49.1 | $-2916.81 |
| ETH | 5197 | 48.0 | 48.6 | $-3403.87 |
| SOL | 5427 | 48.1 | 48.6 | $-3166.26 |
| XRP | 5503 | 48.6 | 48.5 | $-2491.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
