# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 443 windows, 12179 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 223 | 34.5 | 36.1 | $-171.36 | -7.7% | $828.64 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1038 | 51.3 | 50.0 | $-179.94 | -1.7% | $820.06 | -0.6 | done | can't tell from luck |
| trend_filter | 701 | 50.4 | 50.6 | $-329.69 | -4.7% | $670.31 | -1.3 | done | can't tell from luck |
| value_ev10 | 574 | 38.5 | 40.2 | $-436.76 | -7.6% | $563.24 | -1.5 | done | can't tell from luck |
| value_ev5 | 852 | 40.8 | 41.9 | $-532.24 | -6.2% | $467.76 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1229 | 49.6 | 50.0 | $-555.58 | -4.5% | $444.42 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1229 | 50.4 | 51.7 | $-821.36 | -6.7% | $178.64 | -2.5 | done | losing for real |
| coinflip | 1765 | 50.2 | 50.8 | $-888.56 | -5.0% | $111.44 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1038 | 48.7 | 51.8 | $-1055.00 | -10.2% | $-55.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1765 | 49.7 | 51.5 | $-1270.05 | -7.2% | $-270.05 | -3.1 | done | losing for real |
| always_up | 1765 | 45.8 | 50.5 | $-2295.07 | -13.0% | $-1295.07 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2753 | 47.5 | 49.3 | $-2163.78 |
| ETH | 3055 | 47.9 | 48.8 | $-2000.35 |
| SOL | 3160 | 47.7 | 49.3 | $-2583.06 |
| XRP | 3211 | 48.6 | 49.2 | $-1788.42 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
