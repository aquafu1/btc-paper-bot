# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 398 windows, 10900 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 12:00 AM | too few trades (199/200) |
| value_ev10 | 518 | 40.5 | 40.5 | $-164.41 | -3.2% | $835.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 925 | 50.6 | 49.8 | $-231.29 | -2.5% | $768.71 | -0.8 | done | can't tell from luck |
| value_ev5 | 769 | 42.0 | 42.2 | $-300.26 | -3.9% | $699.74 | -0.9 | done | can't tell from luck |
| trend_filter | 618 | 49.8 | 50.6 | $-334.25 | -5.4% | $665.75 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1097 | 49.2 | 49.8 | $-504.17 | -4.6% | $495.83 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1097 | 50.8 | 52.0 | $-683.79 | -6.2% | $316.21 | -2.2 | done | losing for real |
| coinflip | 1584 | 50.0 | 50.8 | $-815.62 | -5.1% | $184.38 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 925 | 49.4 | 52.1 | $-821.35 | -8.9% | $178.65 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1584 | 49.9 | 51.6 | $-1059.06 | -6.7% | $-59.06 | -2.8 | done | losing for real |
| always_up | 1584 | 46.2 | 50.8 | $-1954.00 | -12.3% | $-954.00 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2466 | 47.7 | 49.5 | $-1715.87 |
| ETH | 2735 | 48.0 | 48.9 | $-1668.39 |
| SOL | 2820 | 48.0 | 49.5 | $-2100.52 |
| XRP | 2879 | 48.9 | 49.2 | $-1440.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
