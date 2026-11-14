# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 313 windows, 8379 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 830 | 53.1 | 51.9 | $-153.22 | -1.8% | $846.78 | -0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 684 | 52.8 | 51.8 | $-160.73 | -2.3% | $839.27 | -0.6 | done | can't tell from luck |
| value_ev20 | 155 | 34.2 | 36.6 | $-180.14 | -11.6% | $819.86 | -1.1 | Sun 2:30 AM | too few trades (155/200) |
| value_ev10 | 400 | 38.0 | 40.5 | $-412.57 | -10.3% | $587.43 | -1.8 | done | can't tell from luck |
| value_ev5 | 598 | 39.6 | 42.2 | $-617.40 | -10.3% | $382.60 | -2.2 | done | losing for real |
| trend_filter | 463 | 45.4 | 50.3 | $-658.46 | -14.2% | $341.54 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 684 | 47.2 | 49.9 | $-684.76 | -10.0% | $315.24 | -2.7 | done | losing for real |
| coinflip | 1245 | 50.0 | 50.9 | $-758.45 | -6.1% | $241.55 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 830 | 46.9 | 49.9 | $-837.80 | -10.1% | $162.20 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1245 | 48.6 | 51.3 | $-1170.16 | -9.4% | $-170.16 | -3.5 | done | losing for real |
| always_up | 1245 | 47.3 | 50.5 | $-1289.52 | -10.4% | $-289.52 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1878 | 46.4 | 49.3 | $-1893.26 |
| ETH | 2106 | 46.9 | 48.8 | $-2005.50 |
| SOL | 2179 | 47.9 | 49.4 | $-1785.90 |
| XRP | 2216 | 48.6 | 49.1 | $-1238.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
