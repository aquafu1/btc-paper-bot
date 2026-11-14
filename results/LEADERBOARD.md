# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 315 windows, 8430 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 688 | 53.1 | 51.8 | $-122.15 | -1.8% | $877.85 | -0.5 | done | can't tell from luck |
| value_ev20 | 155 | 34.2 | 36.6 | $-180.14 | -11.6% | $819.86 | -1.1 | Sun 2:45 AM | too few trades (155/200) |
| reversal_15m_0.10pct | 837 | 52.7 | 51.9 | $-223.22 | -2.7% | $776.78 | -0.8 | done | can't tell from luck |
| value_ev10 | 401 | 38.2 | 40.5 | $-402.08 | -10.0% | $597.92 | -1.7 | done | can't tell from luck |
| value_ev5 | 601 | 39.8 | 42.2 | $-606.45 | -10.1% | $393.55 | -2.2 | done | losing for real |
| trend_filter | 467 | 45.0 | 50.3 | $-698.46 | -15.0% | $301.54 | -3.3 | done | losing for real |
| momentum_60m_0.30pct | 688 | 46.9 | 49.9 | $-724.76 | -10.5% | $275.24 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 837 | 47.3 | 49.9 | $-774.34 | -9.3% | $225.66 | -2.7 | done | losing for real |
| coinflip | 1252 | 49.8 | 50.9 | $-789.83 | -6.3% | $210.17 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1252 | 48.4 | 51.3 | $-1221.92 | -9.8% | $-221.92 | -3.6 | done | losing for real |
| always_up | 1252 | 47.6 | 50.5 | $-1226.06 | -9.8% | $-226.06 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1894 | 46.5 | 49.3 | $-1895.12 |
| ETH | 2111 | 46.9 | 48.8 | $-2017.45 |
| SOL | 2192 | 47.9 | 49.4 | $-1802.65 |
| XRP | 2233 | 48.6 | 49.1 | $-1254.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
