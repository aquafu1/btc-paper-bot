# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 73 windows, 1827 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 286 | 56.6 | 51.0 | $+218.16 | +7.6% | $1218.16 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 127 | 61.4 | 52.5 | $+182.65 | +14.4% | $1182.65 | +1.7 | Wed 7:45 PM | too few trades (127/200) |
| reversal_15m_0.10pct | 172 | 56.4 | 51.9 | $+111.83 | +6.5% | $1111.83 | +0.9 | Wed 12:15 PM | too few trades (172/200) |
| value_ev10 | 98 | 43.9 | 39.5 | $+39.52 | +4.0% | $1039.52 | +0.3 | Thu 4:00 AM | too few trades (98/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 7:15 AM | too few trades (41/200) |
| value_ev5 | 137 | 41.6 | 41.1 | $-58.07 | -4.2% | $941.93 | -0.4 | Wed 5:45 PM | too few trades (137/200) |
| trend_filter | 95 | 45.3 | 48.7 | $-99.47 | -10.5% | $900.53 | -1.0 | Thu 5:15 AM | too few trades (95/200) |
| coinflip | 286 | 50.0 | 51.5 | $-179.77 | -6.3% | $820.23 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 172 | 43.6 | 49.4 | $-247.58 | -14.4% | $752.42 | -1.9 | Wed 12:15 PM | too few trades (172/200) |
| momentum_60m_0.30pct | 127 | 38.6 | 48.5 | $-287.99 | -22.7% | $712.01 | -2.5 | Wed 7:45 PM | too few trades (127/200) |
| always_up | 286 | 44.1 | 50.4 | $-450.87 | -15.8% | $549.13 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 379 | 47.8 | 49.8 | $-97.01 |
| ETH | 432 | 46.3 | 48.6 | $-268.84 |
| SOL | 504 | 49.2 | 48.1 | $-242.98 |
| XRP | 512 | 50.4 | 48.3 | $-196.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
