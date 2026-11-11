# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 72 windows, 1796 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 281 | 56.6 | 51.0 | $+208.68 | +7.4% | $1208.68 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 125 | 60.8 | 52.6 | $+160.78 | +12.9% | $1160.78 | +1.5 | Wed 7:45 PM | too few trades (125/200) |
| reversal_15m_0.10pct | 168 | 56.5 | 51.9 | $+112.75 | +6.7% | $1112.75 | +0.9 | Wed 12:30 PM | too few trades (168/200) |
| value_ev10 | 96 | 43.8 | 39.2 | $+41.91 | +4.4% | $1041.91 | +0.4 | Thu 4:15 AM | too few trades (96/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 6:00 AM | too few trades (41/200) |
| value_ev5 | 135 | 41.5 | 41.0 | $-55.68 | -4.1% | $944.32 | -0.4 | Wed 5:45 PM | too few trades (135/200) |
| trend_filter | 95 | 45.3 | 48.7 | $-99.47 | -10.5% | $900.53 | -1.0 | Thu 4:45 AM | too few trades (95/200) |
| coinflip | 281 | 49.8 | 51.4 | $-189.25 | -6.7% | $810.75 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 168 | 43.5 | 49.3 | $-246.99 | -14.7% | $753.01 | -1.9 | Wed 12:30 PM | too few trades (168/200) |
| momentum_60m_0.30pct | 125 | 39.2 | 48.4 | $-267.99 | -21.4% | $732.01 | -2.4 | Wed 7:45 PM | too few trades (125/200) |
| always_up | 281 | 43.4 | 50.4 | $-482.15 | -17.2% | $517.85 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 372 | 47.3 | 49.8 | $-115.06 |
| ETH | 425 | 46.6 | 48.5 | $-236.37 |
| SOL | 497 | 48.9 | 48.1 | $-280.33 |
| XRP | 502 | 50.2 | 48.2 | $-219.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
