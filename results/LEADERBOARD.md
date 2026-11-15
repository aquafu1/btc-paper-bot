# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 399 windows, 10922 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 12:15 AM | too few trades (199/200) |
| value_ev10 | 518 | 40.5 | 40.5 | $-164.41 | -3.2% | $835.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 927 | 50.6 | 49.8 | $-228.19 | -2.5% | $771.81 | -0.8 | done | can't tell from luck |
| value_ev5 | 773 | 42.2 | 42.2 | $-269.93 | -3.5% | $730.07 | -0.8 | done | can't tell from luck |
| trend_filter | 618 | 49.8 | 50.6 | $-334.25 | -5.4% | $665.75 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1098 | 49.3 | 49.8 | $-491.06 | -4.5% | $508.94 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1098 | 50.7 | 52.1 | $-693.79 | -6.3% | $306.21 | -2.2 | done | losing for real |
| coinflip | 1588 | 50.0 | 50.9 | $-816.54 | -5.1% | $183.46 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 927 | 49.4 | 52.1 | $-825.65 | -8.9% | $174.35 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1588 | 49.8 | 51.6 | $-1083.36 | -6.8% | $-83.36 | -2.8 | done | losing for real |
| always_up | 1588 | 46.2 | 50.8 | $-1978.30 | -12.5% | $-978.30 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2470 | 47.7 | 49.5 | $-1709.10 |
| ETH | 2743 | 47.9 | 48.9 | $-1679.06 |
| SOL | 2826 | 48.0 | 49.5 | $-2097.72 |
| XRP | 2883 | 48.9 | 49.2 | $-1456.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
