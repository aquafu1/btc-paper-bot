# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 111 windows, 2846 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 218 | 61.0 | 52.9 | $+286.34 | +13.1% | $1286.34 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 275 | 55.3 | 51.9 | $+122.15 | +4.4% | $1122.15 | +0.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 437 | 52.9 | 50.7 | $+20.41 | +0.5% | $1020.41 | +0.1 | done | can't tell from luck |
| value_ev10 | 145 | 40.0 | 40.7 | $-89.56 | -6.2% | $910.44 | -0.6 | Thu 8:45 AM | too few trades (145/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 3:15 PM | too few trades (50/200) |
| trend_filter | 150 | 41.3 | 49.1 | $-278.02 | -18.5% | $721.98 | -2.3 | Thu 7:15 AM | too few trades (150/200) |
| value_ev5 | 204 | 37.7 | 42.1 | $-279.16 | -13.7% | $720.84 | -1.7 | done | can't tell from luck |
| coinflip | 437 | 49.7 | 51.3 | $-305.23 | -7.0% | $694.77 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 275 | 44.7 | 50.3 | $-379.53 | -13.8% | $620.47 | -2.3 | done | losing for real |
| always_up | 437 | 46.7 | 50.3 | $-463.14 | -10.6% | $536.86 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 218 | 39.0 | 49.2 | $-499.02 | -22.9% | $500.98 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 619 | 45.7 | 49.7 | $-560.52 |
| ETH | 692 | 45.5 | 49.0 | $-671.99 |
| SOL | 757 | 48.6 | 48.6 | $-439.41 |
| XRP | 778 | 50.1 | 49.2 | $-316.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
