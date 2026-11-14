# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 366 windows, 9898 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 9:15 PM | too few trades (189/200) |
| value_ev10 | 480 | 41.2 | 40.4 | $-55.33 | -1.2% | $944.67 | -0.2 | done | can't tell from luck |
| value_ev5 | 709 | 42.5 | 42.0 | $-181.65 | -2.6% | $818.35 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 815 | 49.6 | 49.7 | $-369.36 | -4.5% | $630.64 | -1.3 | done | can't tell from luck |
| trend_filter | 550 | 48.9 | 50.5 | $-403.22 | -7.3% | $596.78 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 983 | 51.5 | 52.1 | $-504.31 | -5.1% | $495.69 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 983 | 48.5 | 49.6 | $-556.80 | -5.7% | $443.20 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 815 | 50.4 | 52.1 | $-559.81 | -6.9% | $440.19 | -2.1 | done | losing for real |
| coinflip | 1458 | 49.9 | 50.8 | $-768.90 | -5.3% | $231.10 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1458 | 49.5 | 51.6 | $-1064.76 | -7.3% | $-64.76 | -2.9 | done | losing for real |
| always_up | 1458 | 45.6 | 50.7 | $-1970.11 | -13.5% | $-970.11 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2219 | 47.3 | 49.3 | $-1743.31 |
| ETH | 2494 | 47.8 | 48.8 | $-1709.45 |
| SOL | 2560 | 48.1 | 49.4 | $-1747.30 |
| XRP | 2625 | 48.8 | 49.1 | $-1218.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
