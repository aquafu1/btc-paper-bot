# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 129 windows, 3253 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 234 | 62.0 | 53.1 | $+336.30 | +14.4% | $1336.30 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 308 | 55.8 | 52.0 | $+154.62 | +5.0% | $1154.62 | +0.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 508 | 52.6 | 50.9 | $-54.50 | -1.1% | $945.50 | -0.2 | done | can't tell from luck |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 7:45 AM | too few trades (61/200) |
| value_ev10 | 171 | 37.4 | 40.4 | $-202.46 | -11.8% | $797.54 | -1.3 | Thu 7:30 AM | too few trades (171/200) |
| coinflip | 508 | 51.0 | 51.1 | $-240.48 | -4.7% | $759.52 | -1.1 | done | can't tell from luck |
| trend_filter | 169 | 40.8 | 48.9 | $-331.43 | -19.6% | $668.57 | -2.5 | Thu 8:00 AM | too few trades (169/200) |
| value_ev5 | 244 | 37.3 | 41.9 | $-363.07 | -14.9% | $636.93 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 308 | 44.2 | 50.1 | $-451.26 | -14.7% | $548.74 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 234 | 38.0 | 49.1 | $-577.49 | -24.7% | $422.51 | -3.8 | done | losing for real |
| always_up | 508 | 46.5 | 50.3 | $-604.00 | -11.9% | $396.00 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 699 | 45.1 | 49.5 | $-811.71 |
| ETH | 802 | 45.1 | 48.7 | $-884.25 |
| SOL | 863 | 48.8 | 48.6 | $-514.24 |
| XRP | 889 | 50.2 | 49.0 | $-306.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
