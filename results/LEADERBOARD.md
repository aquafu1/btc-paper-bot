# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 398 windows, 10914 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 12:15 AM | too few trades (199/200) |
| value_ev10 | 518 | 40.5 | 40.5 | $-164.41 | -3.2% | $835.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 926 | 50.5 | 49.8 | $-241.29 | -2.6% | $758.71 | -0.8 | done | can't tell from luck |
| value_ev5 | 772 | 42.1 | 42.2 | $-283.04 | -3.7% | $716.96 | -0.9 | done | can't tell from luck |
| trend_filter | 618 | 49.8 | 50.6 | $-334.25 | -5.4% | $665.75 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1097 | 49.2 | 49.8 | $-504.17 | -4.6% | $495.83 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1097 | 50.8 | 52.0 | $-683.79 | -6.2% | $316.21 | -2.2 | done | losing for real |
| coinflip | 1587 | 50.0 | 50.9 | $-806.54 | -5.1% | $193.46 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 926 | 49.5 | 52.1 | $-815.65 | -8.8% | $184.35 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1587 | 49.8 | 51.6 | $-1073.36 | -6.8% | $-73.36 | -2.8 | done | losing for real |
| always_up | 1587 | 46.2 | 50.8 | $-1968.30 | -12.4% | $-968.30 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2470 | 47.7 | 49.5 | $-1709.10 |
| ETH | 2735 | 48.0 | 48.9 | $-1668.39 |
| SOL | 2826 | 48.0 | 49.5 | $-2097.72 |
| XRP | 2883 | 48.9 | 49.2 | $-1456.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
