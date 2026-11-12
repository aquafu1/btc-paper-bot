# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 109 windows, 2800 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 214 | 60.3 | 52.9 | $+246.69 | +11.5% | $1246.69 | +1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 272 | 55.1 | 52.0 | $+109.61 | +4.0% | $1109.61 | +0.7 | done | can't tell from luck |
| momentum_5m_0.00pct | 429 | 53.4 | 50.8 | $+61.57 | +1.4% | $1061.57 | +0.3 | done | can't tell from luck |
| value_ev10 | 145 | 40.0 | 40.7 | $-89.56 | -6.2% | $910.44 | -0.6 | Thu 8:00 AM | too few trades (145/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 1:15 PM | too few trades (50/200) |
| trend_filter | 146 | 42.5 | 49.0 | $-238.02 | -16.3% | $761.98 | -1.9 | Thu 7:45 AM | too few trades (146/200) |
| value_ev5 | 200 | 38.0 | 42.0 | $-261.21 | -13.1% | $738.79 | -1.6 | done | can't tell from luck |
| coinflip | 429 | 49.9 | 51.3 | $-279.86 | -6.5% | $720.14 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 272 | 44.9 | 50.2 | $-366.42 | -13.5% | $633.58 | -2.3 | done | losing for real |
| always_up | 429 | 47.6 | 50.3 | $-383.14 | -8.9% | $616.86 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 214 | 39.7 | 49.1 | $-459.02 | -21.4% | $540.98 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 611 | 46.0 | 49.7 | $-515.25 |
| ETH | 677 | 45.9 | 48.9 | $-604.33 |
| SOL | 748 | 48.8 | 48.6 | $-412.16 |
| XRP | 764 | 50.5 | 49.1 | $-251.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
